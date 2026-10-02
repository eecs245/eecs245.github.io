"""Reuse verified Vision transcripts; OCR newly published PDFs on Linux CI."""
from pathlib import Path
import os,json,hashlib,subprocess,tempfile,re
site=Path(os.environ['EECS245_SOURCES'])/'website'
cache=Path(os.environ['EECS245_OCR']);cache.mkdir(parents=True,exist_ok=True)
paths=subprocess.check_output(['git','-C',str(site),'ls-tree','-r','--name-only','HEAD']).decode().splitlines()
for name in paths:
 if not re.match(r'resources/lecture-pdfs/lec\d+-filled\.pdf$',name):continue
 data=subprocess.check_output(['git','-C',str(site),'show','HEAD:'+name]);digest=hashlib.sha256(data).hexdigest()
 target=cache/(Path(name).stem+'.json')
 if target.exists() and json.loads(target.read_text()).get('sha256')==digest:continue
 pages=[]
 with tempfile.TemporaryDirectory() as tmp:
  root=Path(tmp);pdf=root/'source.pdf';pdf.write_bytes(data)
  info=subprocess.check_output(['pdfinfo',str(pdf)]).decode();count=int(re.search(r'Pages:\s*(\d+)',info)[1])
  for number in range(1,count+1):
   text=subprocess.check_output(['pdftotext','-f',str(number),'-l',str(number),str(pdf),'-']).decode();ocr=len(text.strip())<80
   if ocr:
    subprocess.run(['pdftoppm','-f',str(number),'-l',str(number),'-singlefile','-scale-to','2200','-png',str(pdf),str(root/'page')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    text=subprocess.check_output(['tesseract',str(root/'page.png'),'stdout','-l','eng'],stderr=subprocess.DEVNULL).decode()
   pages.append({'page':number,'text':text,'ocr':ocr})
 target.write_text(json.dumps({'sha256':digest,'pages':pages},ensure_ascii=False))
 print('Refreshed OCR:',Path(name).name)
