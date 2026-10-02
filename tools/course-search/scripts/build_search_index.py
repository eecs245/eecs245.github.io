"""Index committed public course sources only; never traverse the private repo."""
from pathlib import Path
import json,re,html,subprocess,hashlib,datetime,os
ROOT=Path(os.environ.get('EECS245_SOURCES','/Users/surajrampure/Desktop/245'))
OUT=Path(__file__).resolve().parents[1]
OCR=Path(os.environ.get('EECS245_OCR',str(OUT.parents[1]/'work/ocr')))
now=datetime.datetime.now(datetime.timezone.utc)
records=[];sources=[];errors=[]
def git(repo,*args):return subprocess.check_output(['git','-C',str(repo),*args])
def files(repo):return git(repo,'ls-tree','-r','--name-only','HEAD').decode().splitlines()
def source(repo,path):
 data=git(repo,'show','HEAD:'+path)
 # A committed public repository is the publication boundary. Use the first
 # addition in reachable history as release evidence, not a guessed class date.
 dates=git(repo,'log','--diff-filter=A','--format=%cI','HEAD','--',path).decode().splitlines()
 date=dates[-1] if dates else git(repo,'log','-1','--format=%cI','HEAD','--',path).decode().strip()
 if datetime.datetime.fromisoformat(date)>now:return None
 sources.append({'repo':repo.name,'path':path,'sha256':hashlib.sha256(data).hexdigest(),'releaseAt':date})
 return data,date
def slug(s):return re.sub(r'[^\w\s-]','',s.lower()).strip().replace(' ','-')
def clean(s):
 s=re.sub(r'<(?:style|script)\b[\s\S]*?</(?:style|script)>','',s,flags=re.I)
 s=re.sub(r'\{%[\s\S]*?%\}|\{\{[\s\S]*?\}\}','',s)
 s=re.sub(r'!\[[^\]]*\]\([^)]*\)','',s)
 s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',s)
 s=re.sub(r'</?(?:span|div|p|img|table|tr|td|th|thead|tbody|strong|em|a|br|h[1-6]|nav|ul|li|ol|blockquote|sup|sub|details|summary)\b[^>]*>',' ',s)
 s=re.sub(r'^\s*:{3,}.*$|^\s*:[a-z][^\n]*$', '', s, flags=re.M)
 s=re.sub(r'\*\*([uvw])\*\*',lambda m:'$\\vec{'+m[1]+'}$',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'\1',s)
 return re.sub(r'\s+',' ',html.unescape(s)).strip(' #*`\n')
def concepts(raw):
 raw=raw.replace('\\\\','\\')
 tags=[]
 # Formula evidence bridges natural language to math; cdot alone could mean
 # scalar multiplication, so require two vector operands or vector transpose.
 vec=r'(?:\\(?:vec|mathbf|boldsymbol)\s*\{?[a-zA-Z]\}?|[uvwxab])'
 if re.search(vec+r'\s*(?:\\cdot|·|•)\s*'+vec,raw) or re.search(vec+r'\s*\^\s*\{?(?:T|\\top)\}?\s*'+vec,raw):tags+=['dot product','inner product']
 if re.search(r'\\(?:lVert|Vert|norm)|\|\|',raw):tags+=['vector norm magnitude length']
 if re.search(r'\\(?:nabla|grad)',raw):tags+=['gradient partial derivatives']
 if re.search(r'\\lambda|Av\s*=\s*λ|eigen',raw,re.I):tags+=['eigenvalues eigenvectors']
 if re.search(r'\\(?:proj|operatorname\{proj)',raw):tags+=['orthogonal projection closest vector']
 return tags
def add(cat,title,section,text,url,date,semester='Fall 2026',detail=''):
 text=clean(text)
 if len(text)<20:return
 # Overlapping chunks ensure the 256-token embedding sees every passage.
 math=[(m.start(),m.end()) for m in re.finditer(r'\$\$[\s\S]*?\$\$|\$[^$]+\$|\\\\?\([\s\S]*?\\\\?\)|\\\\?\[[\s\S]*?\\\\?\]',text)]
 for start in range(0,len(text),800):
  left=max(0,start-120);right=min(len(text),start+1000)
  left=text.rfind(' ',0,left)+1
  next_space=text.find(' ',right)
  if next_space>=0:right=next_space
  for a,b in math:
   if a<left<b:left=a
   if a<right<b:right=b
  chunk=text[left:right]
  records.append(dict(id=str(len(records)),category=cat,title=clean(title),section=clean(section),text=chunk,url=url,releaseAt=date,semester=semester,detail=detail,concepts=concepts(chunk)))
def sections(cat,title,content,base,date,semester='Fall 2026',only_problems=False):
 content=re.sub(r'<h2\s+id="([^"]+)"[^>]*>([\s\S]*?)</h2>',lambda m:'\n## '+clean(m[2])+'|ANCHOR|'+m[1]+'\n',content)
 parts=re.split(r'(?m)^(##\s+.+)$' if only_problems else r'(?m)^(#{2,3}\s+.+)$',content)
 if len(parts)==1:add(cat,title,title,content,base,date,semester);return
 for i in range(1,len(parts),2):
  heading=parts[i].lstrip('# ');anchor=slug(heading)
  if '|ANCHOR|' in heading:heading,anchor=heading.split('|ANCHOR|')
  if cat=='Labs' and re.match(r'Recap\b',heading,re.I):continue
  if only_problems and not re.match(r'(Problem\s+\d|Activity\s+\d|Recap)',heading):continue
  add(cat,title,heading,parts[i+1] if i+1<len(parts) else '',base+'#'+anchor,date,semester)
# Canonical MyST page slugs, from the course TOC (not generated draft notebooks).
repo=ROOT/'notes'; toc=git(repo,'show','HEAD:myst.yml').decode()
for path in re.findall(r'file:\s*(\S+\.ipynb)',toc):
 if path=='index.ipynb':continue
 data,date=source(repo,path);nb=json.loads(data)
 content='\n\n'.join(''.join(c['source']) for c in nb['cells'] if c['cell_type']=='markdown')
 title=(re.search(r'^#\s+(.+)',content,re.M) or [None,Path(path).stem])[1]
 group=re.sub(r'^\d+_','',Path(path).parent.name).replace('_','-')
 # Appendix uses the published math-foundations slug.
 base='https://notes.eecs245.org/'+group+'/'+Path(path).stem[3:]+'/'
 exported=repo/'_build/html'/f'{group}.{Path(path).stem[3:]}.json'
 if exported.exists():base='https://notes.eecs245.org/'+json.loads(exported.read_text())['slug'].replace('.','/')+'/'
 sections('Notes',title,content,base,date)
# Assignment / exam HTML is the primary student-facing source; no dirty edits.
for cat,repo,prefix,host in [('Homeworks',ROOT/'website','resources/homeworks/','https://eecs245.org/'),('Labs',ROOT/'website','resources/labs/','https://eecs245.org/')]:
 for path in files(repo):
  if not(path.startswith(prefix) and path.endswith('/index.md')):continue
  data,date=source(repo,path);content=data.decode()
  match=re.search(r'^title:\s*["\']?(.+?)["\']?$',content,re.M);title=match[1] if match else Path(path).parent.name
  semester=next((name for code,name in [('fa25','Fall 2025'),('wn26','Winter 2026'),('sp26','Spring 2026')] if code in path),'Fall 2026')
  sections(cat,title,content,host+str(Path(path).parent)+'/',date,semester,True)
# Current published exam pages are composed from committed per-question sources.
examrepo=Path(os.environ.get('EECS245_EXAMS',str(OUT.parents[1]/'work/public-sources/exams')))
for path in sorted((examrepo/'.build/exams').glob('*/index.md')):
 content=path.read_text();title=re.search(r'^title:\s*"(.+)"$',content,re.M)[1]
 if re.search(r'practice|mock',title+' '+path.parent.name,re.I):continue
 dates=[source(examrepo,p)[1] for p in files(examrepo) if p.startswith('src/'+path.parent.name+'/') and p.endswith(('src.md','config.yml'))]
 date=max(dates)
 sections('Past exams',title,content,'https://exams.eecs245.org/exams/'+path.parent.name+'/',date,title.split(' Midterm')[0].split(' Final')[0],True)
# Lecture schedule names + every page: text layer when available, local Vision
# OCR otherwise. OCR transcripts are explicitly marked and can be imperfect.
repo=ROOT/'website';schedule='\n'.join(git(repo,'show','HEAD:'+p).decode() for p in files(repo) if p.startswith('_modules/') and p.endswith('.md'))
lectures={}
for block in re.split(r'\n  - date:',schedule)[1:]:
 lec=re.search(r'name: LEC (\d+)',block);pdf=re.search(r'live_notes: (resources/lecture-pdfs/[^\s]+)',block);title=re.search(r'\n\s+title:\s*(.+)',block)
 if lec and pdf and title:lectures[pdf[1]]='Lecture '+lec[1]+' · '+title[1].strip('"\'')
ocrpages=0
for path,title in lectures.items():
 data,date=source(repo,path);url='https://eecs245.org/'+path
 cache=OCR/(Path(path).stem+'.json')
 if not cache.exists():errors.append('Missing OCR: '+path);continue
 pages=json.loads(cache.read_text())['pages']
 for page in pages:
  ocrpages+=page['ocr'];add('Lecture PDFs',title,'Page '+str(page['page']),page['text'],url+'#page='+str(page['page']),date,detail='OCR · check original PDF' if page['ocr'] else 'PDF text')
metadata={'builtAt':now.isoformat(),'releaseMetadata':'first addition in committed public repository history','commits':{name:git(examrepo if name=='exams' else ROOT/name,'rev-parse','HEAD').decode().strip() for name in ['notes','website','exams']},'documents':len({r['url'].split('#')[0] for r in records}),'records':len(records),'ocrPages':ocrpages,'categories':{cat:sum(r['category']==cat for r in records) for cat in ['Notes','Lecture PDFs','Homeworks','Labs','Past exams']},'errors':errors}
(OUT/'search-index.json').write_text(json.dumps({'records':records,'metadata':metadata},ensure_ascii=False))
(OUT/'source-manifest.json').write_text(json.dumps({'metadata':metadata,'sources':sources},indent=2))
print(json.dumps(metadata,indent=2))
if errors:raise SystemExit('Incomplete corpus: see coverage errors')
