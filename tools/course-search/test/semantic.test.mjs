import {test,before} from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {pipeline,env} from '@huggingface/transformers';
import {createQueryProcessor,buildSearch,mergeResults} from '../public/search.mjs';
import {semanticSearch} from '../public/semantic.mjs';
let records,vectors,embed,processQuery,keyword;
const cache=new Map();
before(async()=>{
 env.allowRemoteModels=false;env.localModelPath=new URL('../public/models/',import.meta.url).pathname;
 const data=JSON.parse(await readFile(new URL('../public/data/index.json',import.meta.url)));
 records=data.records;
 processQuery=createQueryProcessor(records);keyword=buildSearch(records);
 assert.equal(data.metadata.errors.length,0);
 assert(records.every(r=>new Date(r.releaseAt)<=new Date(data.metadata.builtAt)));
 assert(records.every(r=>!r.url.includes('private')&&!r.url.includes('fa26-mt')));
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
