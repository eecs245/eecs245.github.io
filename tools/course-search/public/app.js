import {resultCategories,combineLectureResults,tokens,buildSearch,excerpt,sortDocuments,createQueryProcessor,normalizeQuery,mergeResults,filterCategories,indexedCoverage} from './search.mjs';
import {recordingPreviews} from './recording-previews/previews.mjs';
if(new URLSearchParams(location.search).has('embedded'))document.body.classList.add('embedded');
const input=document.querySelector('#search'),groups=document.querySelector('#groups');
if(document.body.classList.contains('embedded')){
 window.addEventListener('message',event=>{if(event.origin===location.origin&&event.source===parent&&event.data?.type==='eecs245-search-focus')input.focus();});
 document.addEventListener('keydown',event=>{if(event.key==='Escape'){event.preventDefault();parent.postMessage({type:'eecs245-search-close'},location.origin);}if((event.metaKey||event.ctrlKey)&&event.key.toLowerCase()==='f'){event.preventDefault();input.focus();}});
}

let search=null,allResults=[],timer,requestId=0,semanticReady=false,semanticFailed=false;
let processQuery=null,activeQuery='',sortOrder='relevance',lastQuery='';
const semanticCache=new Map();
const correction=document.createElement('p');correction.className='search-correction';correction.hidden=true;correction.setAttribute('role','status');correction.setAttribute('aria-live','polite');document.querySelector('#search-form').after(correction);
const expandedCategories=new Set(),expandedNotes=new Set(),expandedRecordings=new Set();
const worker=new Worker(new URL("./worker.js",import.meta.url),{type:"module"});
worker.onmessage=({data})=>{
 if(data.type==="ready"){semanticReady=true;run();}
 if(data.type==="results"){
  semanticCache.delete(data.query);semanticCache.set(data.query,data.results);
  if(semanticCache.size>32)semanticCache.delete(semanticCache.keys().next().value);
  if(data.id===requestId&&data.query===activeQuery)display(mergeResults(search(activeQuery,{correct:false}),data.results));
 }
 if(data.type==="error"){document.querySelector('#timing').title=data.message;semanticFailed=true;document.querySelector("#timing").textContent="Keyword search";}
};
worker.onerror=()=>{semanticFailed=true;document.querySelector("#timing").textContent="Keyword search";};
const icons=['▶','▤','▦','◫','▥'];
const selected=new Set(resultCategories);
function documentLabel(record){
 if(record.category==='Homeworks'||record.category==='Labs') return record.title.split(':')[0];
 return record.title;
}
function locationLabel(location){
 const numbered=location.section.match(/^(Problem|Activity|Page)\s+(\d+)/);
 return numbered ? (numbered[1]==='Problem'?'P':numbered[1]==='Activity'?'A':'p.')+numbered[2] : location.section;
}
function highlight(node,text,query){
 const terms=tokens(query);for(const part of text.split(/([a-z0-9]+)/gi)){
  if(terms.some(t=>tokens(part)[0]===t||part.toLowerCase().startsWith(t))){const mark=document.createElement('mark');mark.textContent=part;node.append(mark);}else node.append(document.createTextNode(part));
 }
}
function render(){
 groups.replaceChildren();
 for(const [i,category] of resultCategories.entries()){
  const matches=sortDocuments(allResults.filter(r=>r.category===category),sortOrder);if(!matches.length)continue;
  const section=document.createElement('section');section.className='group';section.dataset.category=category;
  const head=document.createElement('div');head.className='group-head';
  const icon=document.createElement('span');icon.className='group-icon';icon.textContent=icons[i];
  const h2=document.createElement('h2');h2.textContent=category;
  const count=document.createElement('span');count.className='group-count';count.textContent=matches.length;
  head.append(icon,h2,count);section.append(head);
  const cards=document.createElement('div');cards.className='cards';
  for(const r of expandedCategories.has(category)?matches:matches.slice(0,3)){
   const card=document.createElement('article');card.className='card';
   const heading=document.createElement('h3');const title=document.createElement('a');title.href=r.url;title.target='_blank';title.rel='noreferrer';title.textContent=documentLabel(r);title.title=r.title;heading.append(title);
   const locations=document.createElement('div');locations.className='locations';locations.setAttribute('aria-label','Matching locations');
   for(const location of r.locations){
    const link=document.createElement('a');link.href=location.url;link.target='_blank';link.rel='noreferrer';link.title=location.section;
    link.textContent=locationLabel(location);if(window.renderMathInElement)window.renderMathInElement(link,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false,trust:false});link.setAttribute('aria-label',r.title+' · '+location.section);
    locations.append(link);
   }
   const details=document.createElement('details');details.className='passages';
   const summary=document.createElement('summary');summary.textContent='Details';summary.setAttribute('aria-label','Preview passages from '+r.title);details.append(summary);
   for(const location of r.locations){
    const passage=document.createElement('div');passage.className='passage';
    const link=document.createElement('a');link.href=location.url;link.target='_blank';link.rel='noreferrer';link.textContent=location.section+' ↗';
    const text=document.createElement('p');text.className='card-excerpt';
    if(/\\|\$/.test(location.text)){
     text.textContent=location.text.replace(/\\\\/g,'\\').replace(/\\(?:mathbf|boldsymbol|bm)\s*\{([a-zA-Z](?:_\{?\d+\}?)?)\}/g,'\\vec{$1}').replace(/\*\*([uvw])\*\*/g,'$\\vec{$1}$');
     if(window.renderMathInElement)window.renderMathInElement(text,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false},{left:'\\(',right:'\\)',display:false},{left:'\\[',right:'\\]',display:true}],throwOnError:false,trust:false,macros:{'\\v':'\\vec{#1}','\\R':'\\mathbb{R}'}});
    }else highlight(text,excerpt(location.text,activeQuery),activeQuery);
    if(location.detail.startsWith('OCR')){const quality=document.createElement('small');quality.textContent='OCR transcript · check original PDF';text.append(quality);}
    passage.append(link,text);details.append(passage);
   }
   if(category==='Notes'){
    card.classList.add('note-card');
    const note=document.createElement('details');note.className='note-sections';note.open=expandedNotes.has(r.id);
    note.addEventListener('toggle',()=>{note.open?expandedNotes.add(r.id):expandedNotes.delete(r.id);});
    const toggle=document.createElement('summary');toggle.className='note-title';toggle.textContent=documentLabel(r);
    const open=document.createElement('a');open.className='open-note';open.href=r.url;open.target='_blank';open.rel='noreferrer';open.textContent='Open note ↗';
    note.append(toggle,open,locations,details);card.append(note);
   }else if(category==='Lectures'){
    card.classList.add('recording-card');
    const recording=document.createElement('details');recording.className='recording-moments';recording.open=expandedRecordings.has(r.id);
    recording.addEventListener('toggle',()=>{recording.open?expandedRecordings.add(r.id):expandedRecordings.delete(r.id);});
    const toggle=document.createElement('summary');toggle.className='recording-summary';
    const thumbnail=document.createElement('span');thumbnail.className='recording-thumbnail';thumbnail.setAttribute('aria-hidden','true');
    const id=r.recording?new URL(r.recording.url).pathname.split('/').pop():null;
    if(recordingPreviews[id]){const image=document.createElement('img');image.src=recordingPreviews[id];image.alt='';image.loading='lazy';thumbnail.append(image);}
    const play=document.createElement('span');play.className='recording-play';play.textContent=r.recording?'▶':'▧';thumbnail.append(play);
    const label=document.createElement('span');label.className='recording-label';label.textContent=documentLabel(r);
    const preview=document.createElement('span');preview.className='card-excerpt';const previewLocations=(r.recording||r.pdf).locations;highlight(preview,excerpt(previewLocations.reduce((best,l)=>l.score>best.score?l:best).text,activeQuery),activeQuery);
    const countLabel=(count,singular)=>`${count} ${singular}${count===1?'':'s'}`;
    const counts=[r.recording&&countLabel(r.recording.locations.length,'moment'),r.pdf&&countLabel(r.pdf.locations.length,'PDF page')].filter(Boolean);
    const prompt=document.createElement('span');prompt.className='recording-prompt';prompt.textContent=counts.join(' · ')+' · Show matches';
    toggle.append(thumbnail,label,preview,prompt);
    const content=document.createElement('div');content.className='recording-content';
    for(const [source,label] of [[r.recording,'Watch recording'],[r.pdf,'Open lecture PDF']]){
     if(!source)continue;
     const sourceBlock=document.createElement('section');sourceBlock.className='lecture-source';
     const open=document.createElement('a');open.className='open-recording';open.href=source.url;open.target='_blank';open.rel='noreferrer';open.textContent=label+' ↗';
     const sourceLocations=document.createElement('div');sourceLocations.className='locations';sourceLocations.setAttribute('aria-label',source.category==='Lecture recordings'?'Matching recording timestamps':'Matching PDF pages');
     for(const link of [...locations.children])if(source.locations.some(location=>location.url===link.href||location.url===link.getAttribute('href')))sourceLocations.append(link);
     sourceBlock.append(open,sourceLocations);content.append(sourceBlock);
    }
    content.append(details);recording.append(toggle,content);card.append(recording);
   }else {
    card.append(heading);
    card.append(locations,details);
   }
   cards.append(card);
  }
  section.append(cards);
  if(matches.length>3){
   const more=document.createElement('button');more.type='button';more.className='show-more';
   more.textContent=expandedCategories.has(category)?'Show less':`Show more (${matches.length-3})`;
   more.setAttribute('aria-label',`${more.textContent} ${category.toLowerCase()}`);
   more.setAttribute('aria-expanded',String(expandedCategories.has(category)));
   more.addEventListener('click',()=>{expandedCategories.has(category)?expandedCategories.delete(category):expandedCategories.add(category);render();});
   section.append(more);
  }
  groups.append(section);
 }
}
function display(results){
 const query=input.value.trim();allResults=combineLectureResults(filterCategories(results,selected));
 document.querySelector('#summary').textContent=`${allResults.length} documents · ${allResults.reduce((sum,r)=>sum+r.locations.length,0)} matching locations for “${query}”`;
 document.querySelector('#timing').textContent=semanticFailed?'Keyword search':semanticCache.has(activeQuery)?'':semanticReady?'Finding related results…':'Preparing semantic search…';
 document.querySelector('#empty').hidden=!!allResults.length;
 document.querySelector('#empty h2').textContent=selected.size?'No matches yet.':'Select a category to search.';
 document.querySelector('#empty p').textContent=selected.size?'Try another topic or enable more categories.':'Use the buttons above to include course materials.';render();
}
function run(){
 const query=input.value.trim();requestId++;document.body.classList.toggle('has-query',!!query);document.querySelector('#results').hidden=!query;correction.hidden=true;if(!query){activeQuery='';return;}
 if(!search){document.querySelector('#summary').textContent='Loading the course index…';return;}
 const processed=processQuery(query);activeQuery=processed.normalized;
 if(activeQuery!==lastQuery){expandedCategories.clear();expandedNotes.clear();expandedRecordings.clear();lastQuery=activeQuery;}
 if(processed.corrections.length){correction.textContent=`Showing results for “${normalizeQuery(processed.corrected)}”.`;correction.hidden=false;}
 const keyword=search(activeQuery,{correct:false});
 if(semanticCache.has(activeQuery)){display(mergeResults(keyword,semanticCache.get(activeQuery)));return;}
 display(keyword);
 if(semanticReady)worker.postMessage({query:activeQuery,id:requestId});
}
for(const button of document.querySelectorAll('[data-category]')) button.addEventListener('click',()=>{
 const category=button.dataset.category;selected.has(category)?selected.delete(category):selected.add(category);
 button.setAttribute('aria-pressed',String(selected.has(category)));run();
});
for(const button of document.querySelectorAll('[data-sort]'))button.addEventListener('click',()=>{sortOrder=button.dataset.sort;for(const b of document.querySelectorAll('[data-sort]'))b.setAttribute('aria-pressed',String(b===button));render();});
input.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(run,60);});
document.querySelector('#search-form').addEventListener('submit',e=>{e.preventDefault();clearTimeout(timer);run();});
document.addEventListener('keydown',e=>{if(e.key==='/'&&e.target!==input){e.preventDefault();input.focus();}});
try{
 const response=await fetch('./data/index.json');if(!response.ok)throw new Error();const data=await response.json();search=buildSearch(data.records);processQuery=createQueryProcessor(data.records);
 document.querySelector('#index-coverage').textContent=indexedCoverage(data.records);
 run();
}catch{document.querySelector('#results').hidden=false;document.querySelector('#summary').textContent='Search is unavailable. Refresh to try again.';}
