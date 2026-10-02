import {test,before} from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {pipeline,env} from '@huggingface/transformers';
import {normalizeQuery} from '../public/search.mjs';
import {semanticSearch} from '../public/semantic.mjs';
let records,vectors,embed;
before(async()=>{
 env.allowRemoteModels=false;env.localModelPath=new URL('../public/models/',import.meta.url).pathname;
 const data=JSON.parse(await readFile(new URL('../public/data/index.json',import.meta.url)));
 records=data.records;
 assert.equal(data.metadata.errors.length,0);
 assert(records.every(r=>new Date(r.releaseAt)<=new Date(data.metadata.builtAt)));
 assert(records.every(r=>!r.url.includes('private')&&!r.url.includes('fa26-mt')));
 const bytes=await readFile(new URL('../public/data/vectors.f32',import.meta.url));
 vectors=new Float32Array(bytes.buffer,bytes.byteOffset,bytes.length/4);
 assert.equal(vectors.length,records.length*384);
 embed=await pipeline('feature-extraction','Xenova/all-MiniLM-L6-v2',{dtype:'q8'});
});
async function search(query){query=normalizeQuery(query);const e=await embed(query,{pooling:'mean',normalize:true});return semanticSearch(records,vectors,query,e.data);}
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
