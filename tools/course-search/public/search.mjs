export const categories=['Notes','Lecture PDFs','Homeworks','Labs','Past exams'];
const aliases={proj:'projection',project:'projection',projecting:'projection',projections:'projection',orthogonality:'orthogonal',perpendicular:'orthogonal',perpendicularity:'orthogonal',perpendicularly:'orthogonal',independent:'independence',dependent:'dependence',vectors:'vector',matrices:'matrix',norms:'norm',bases:'basis'};
const ignored=new Set('what are you looking for the a an is of to in how why about explain me'.split(' '));
export const tokens=text=>(text.toLowerCase().match(/[a-z0-9]+/g)||[]).map(t=>Object.hasOwn(aliases,t)?aliases[t]:t).filter(t=>!ignored.has(t));
export function buildSearch(records){
  const prepared=records.map(r=>({...r,words:tokens(`${r.section} ${r.text}`),heading:tokens(`${r.title} ${r.section}`)}));
  const postings=new Map();
  prepared.forEach((r,i)=>{for(const word of new Set(r.words)){if(!postings.has(word))postings.set(word,new Set());postings.get(word).add(i);}});
  return query=>{
    const terms=[...new Set(tokens(query))];if(!terms.length)return [];
    const matches=terms.map(term=>{
      const hits=new Set();for(const [word,ids] of postings)if(word===term||(term.length>=3&&word.startsWith(term)))for(const id of ids)hits.add(id);
      return hits;
    });
    const ids=[...matches[0]].filter(id=>matches.every(hit=>hit.has(id)));
    const ranked=ids.map(id=>{const r=prepared[id];return {...r,score:terms.reduce((s,t)=>s+r.heading.filter(w=>w===t||w.startsWith(t)).length*5+r.words.filter(w=>w===t||w.startsWith(t)).length,0)};}).sort((a,b)=>b.score-a.score);
    return groupDocuments(ranked);
  };
}
export function excerpt(text,query){
  const terms=tokens(query);const words=[...text.matchAll(/[a-z0-9]+/gi)];
  const hit=words.find(m=>terms.some(t=>tokens(m[0])[0]===t||m[0].toLowerCase().startsWith(t)));
  const start=hit?Math.max(0,hit.index-90):0;
  const boundary=start>0?text.indexOf(' ',start):0;
  const offset=boundary>=0?boundary:start;
  let s=text.slice(offset,offset+245).trim();if(offset>0)s='… '+s;if(offset+245<text.length)s+=' …';return s;
}

export function groupDocuments(ranked) {
  const documents=new Map();
  for(const hit of ranked){
    const url=hit.url.split('#')[0];
    const key=`${hit.category}:${url}`;
    if(!documents.has(key)) documents.set(key,{id:key,category:hit.category,title:hit.title,url,semester:hit.semester,detail:hit.detail,score:hit.score,locations:[]});
    const document=documents.get(key);
    // Several index chunks can refer to one section. Retain its best passage.
    if(!document.locations.some(location=>location.url===hit.url)) document.locations.push(hit);
  }
  return [...documents.values()].map(document=>({...document,locations:document.locations.sort((a,b)=>Number(a.id)-Number(b.id))}));
}

// Within a category, chronological means course order for notes/assignments,
// and oldest term first for past exams, followed by MT1, MT2, then the final.
export function sortDocuments(documents,order='relevance'){
 const natural=new Intl.Collator('en',{numeric:true,sensitivity:'base'});
 const key=r=>{
  if(r.category==='Past exams'){
   const year=Number(r.title.match(/20\d{2}/)?.[0]||0);
   const term=/Winter/i.test(r.title)?1:/Spring/i.test(r.title)?2:3;
   const assessment=/Midterm 1/i.test(r.title)?1:/Midterm 2/i.test(r.title)?2:3;
   return year*100+term*10+assessment;
  }
  return /^Appendix/i.test(r.title)?1000:0;
 };
 return [...documents].sort((a,b)=>order==='chronological'?key(a)-key(b)||natural.compare(a.title,b.title):b.score-a.score||natural.compare(a.title,b.title));
}

export function normalizeQuery(query){return query.toLowerCase().replace(/\b(?:perpendicular|perpendicularity|perpendicularly|orthogonality)\b/g,'orthogonal');}
