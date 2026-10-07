import {test,before} from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {pipeline,env} from '@huggingface/transformers';
import {createQueryProcessor,buildSearch,mergeResults} from '../public/search.mjs';
import {semanticSearch} from '../public/semantic.mjs';
import {createHybridSearch} from '../public/hybrid.mjs';
import {parseResourceQuery} from '../public/resource-query.mjs';
let records,vectors,embed,processQuery,keyword;
const cache=new Map();
before(async()=>{
 env.allowRemoteModels=false;env.localModelPath=new URL('../public/models/',import.meta.url).pathname;
 const data=JSON.parse(await readFile(new URL('../public/data/index.json',import.meta.url)));
 records=data.records;
 processQuery=createQueryProcessor(records);keyword=buildSearch(records);
 assert.equal(data.metadata.errors.length,0);
 assert(records.every(r=>new Date(r.releaseAt)<=new Date(data.metadata.builtAt)));
 // Fall 2026 Midterm 1 is now publicly released; other midterms remain excluded.
 assert(records.every(r=>!r.url.includes('private')&&(!r.url.includes('fa26-mt')||r.url.startsWith('https://exams.eecs245.org/exams/fa26-mt1/'))));
 const bytes=await readFile(new URL('../public/data/vectors.f32',import.meta.url));
 vectors=new Float32Array(bytes.buffer,bytes.byteOffset,bytes.length/4);
 assert.equal(vectors.length,records.length*384);
 embed=await pipeline('feature-extraction','Xenova/all-MiniLM-L6-v2',{dtype:'q8'});
});
async function search(query){query=processQuery(query).normalized;if(!cache.has(query)){const e=await embed(query,{pooling:'mean',normalize:true});cache.set(query,semanticSearch(records,vectors,query,e.data));}return cache.get(query);}
test('dot product finds formula-only exam questions and groups every document once',async()=>{
 const found=await search('dot product');
 assert(found.some(d=>d.category==='Past exams'&&d.locations.some(l=>l.formula&&!/dot product/i.test(l.text))));
 const exam=found.find(d=>d.url.endsWith('/fa25-mt1/'));assert(exam.locations.some(l=>l.url.includes('problem-4-mission-impossible')));
 assert.equal(new Set(found.map(d=>d.url)).size,found.length);
 assert(found.every(d=>new Set(d.locations.map(l=>l.url)).size===d.locations.length));
});
test('meaning finds projections without naming the topic',async()=>{
 const found=await search('closest vector on a line');
 assert(found.some(d=>d.url.includes('/projecting-onto-a-single-vector/')));
});
test('prediction mistakes retrieves loss functions without matching exact words',async()=>{
 const found=await search('how do you minimize prediction mistakes');
 assert(found.some(d=>d.url.includes('squared-loss-constant-model')));
});
test('an unrelated semantic query has no results',async()=>{assert.equal((await search('purple flying giraffes')).length,0);});

test('perpendicular and orthogonal return identical documents and locations',async()=>{
 const summarize=results=>results.map(r=>({id:r.id,locations:r.locations.map(l=>l.url)}));
 assert.deepEqual(summarize(await search('perpendicular')),summarize(await search('orthogonal')));
});

test('real local model retrieves a synthetic transcript by meaning',async()=>{
 const fixture=[{id:'caption-fixture',category:'Lecture recordings',title:'Lecture 2 · Synthetic test',section:'0:10–0:40',text:'We choose the median because it minimizes the sum of absolute differences between predictions and observed values.',concepts:[],detail:'Synthetic test only',url:'https://leccap.engin.umich.edu/leccap/player/r/fixture?start=5',start:10,end:40}];
 const document=await embed(fixture.map(r=>`${r.section}. . ${r.text}`),{pooling:'mean',normalize:true});
 const query='minimizing absolute prediction error';
 const embedding=await embed(query,{pooling:'mean',normalize:true});
 const found=semanticSearch(fixture,document.data,query,embedding.data);
 assert.equal(found.length,1);assert.equal(found[0].category,'Lecture recordings');
 assert.equal(found[0].locations[0].url,'https://leccap.engin.umich.edu/leccap/player/r/fixture?start=5');
});

test('semantic and fused results agree for case, loss aliases, and misspellings',async()=>{
 const expected=await search('absolute loss');
 const fused=mergeResults(keyword('absolute loss'),expected);
 for(const query of ['Absolute','ABSOLUTE LOSS','mean absolute error','MAE','absolte loss']) {
  assert.deepEqual(await search(query),expected,query);
  assert.deepEqual(mergeResults(keyword(query),await search(query)),fused,query);
 }
 assert(fused.some(document=>document.url.includes('/absolute-loss/')));
 const keywordLocations=keyword('absolute loss').flatMap(document=>document.locations.map(location=>location.url));
 const fusedLocations=new Set(fused.flatMap(document=>document.locations.map(location=>location.url)));
 assert(keywordLocations.every(url=>fusedLocations.has(url)));
 for(const [query,canonical] of [['MSE','squared loss'],['inner product','dot product'],['orthoganol','orthogonal'],['porjection','projection']]) assert.deepEqual(await search(query),await search(canonical),query);
});

test('published Lecture 2 captions find absolute loss near 27:10',async t=>{
 const rows=records.filter(r=>r.category==='Lecture recordings'&&r.recordingId==='ucCtbs');
 if(!rows.length){t.skip('Lecture 2 captions are not cached in this snapshot');return;}
 const found=mergeResults(keyword('absolute loss'),await search('absolute loss'));
 const lecture=found.find(d=>d.category==='Lecture recordings'&&d.url.endsWith('/ucCtbs'));
 assert(lecture,'Lecture 2 must be retrieved');
 const moment=lecture.locations.find(l=>l.start<=1630.2&&l.end>=1630.2&&/absolute loss/i.test(l.text));
 assert(moment,'The original caption at 27:10 must remain searchable');
 assert.equal(Number(new URL(moment.url).searchParams.get('start')),Math.max(0,Math.floor(moment.start)-5));
 assert.equal(found.filter(d=>d.url===lecture.url).length,1);
});


test('real hybrid search combines lexical and semantic matches and scopes course resources',async()=>{
 const hybrid=createHybridSearch(records,vectors);
 async function find(input){
  const request=parseResourceQuery(processQuery(input).normalized);
  const embedding=request.query?(await embed(request.query,{pooling:'mean',normalize:true})).data:undefined;
  return hybrid(request,embedding);
 }
 for(const query of ['HW 4 problem 3','hw04 p3','HW4P3']){
  const found=await find(query);assert.equal(found.length,1,query);
  assert(found[0].title.startsWith('Homework 4:'));
  assert(found[0].locations.every(l=>l.url.includes('#problem-3-')));
 }
 const lecture=await find('lecture 8 projection');assert(lecture.length);
 assert(lecture.every(r=>r.title.startsWith('Lecture 8 ·')));
 const lab=await find('lab 4 activity 2');assert.equal(lab.length,1);
 assert(lab[0].locations.every(l=>/^Activity 2\b/.test(l.section)));
 const note=await find('note 3.4 closest vector on a line');assert.equal(note.length,1);
 assert(note[0].url.includes('/projecting-onto-a-single-vector/'));
 const exam=await find('fa25-mt1 problem 4');assert.equal(exam.length,1);
 assert(exam[0].url.endsWith('/fa25-mt1/'));
 assert(exam[0].locations.every(l=>l.url.includes('problem-4-mission-impossible')));
 assert.equal((await find('homework 99 projection')).length,0);
 assert.equal((await find('purple flying giraffes')).length,0);
 const lexical=await find('mission impossible');assert(lexical.some(r=>r.locations.some(l=>l.keyword&&l.section.includes('Mission Impossible'))));
 const meaning=await find('how do you minimize prediction mistakes');assert(meaning.some(r=>r.url.includes('squared-loss-constant-model')));
 const expected=await find('absolute loss');
 for(const alias of ['absolute','MAE','absolte loss'])assert.deepEqual(await find(alias),expected,alias);
});
