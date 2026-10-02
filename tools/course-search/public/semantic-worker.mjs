import {pipeline,env} from '@huggingface/transformers';
import {semanticSearch} from './semantic.mjs';
import {normalizeQuery} from './search.mjs';
env.allowRemoteModels=false;env.allowLocalModels=true;env.localModelPath=new URL('./models/',self.location.href).href;
env.backends.onnx.wasm.wasmPaths=new URL('./vendor/onnx/',self.location.href).href;
env.backends.onnx.wasm.numThreads=1;
let records,vectors,embed;
const ready=(async()=>{
 const [index,binary]=await Promise.all([fetch('./data/index.json').then(r=>{if(!r.ok)throw Error('Index unavailable');return r.json();}),fetch('./data/vectors.f32').then(r=>{if(!r.ok)throw Error('Vectors unavailable');return r.arrayBuffer();})]);
 records=index.records;vectors=new Float32Array(binary);if(vectors.length!==records.length*384)throw Error('Index/vector mismatch');
 embed=await pipeline('feature-extraction','Xenova/all-MiniLM-L6-v2',{dtype:'q8',device:'wasm'});
 self.postMessage({type:'ready'});
})();
ready.catch(error=>self.postMessage({type:'error',message:String(error)}));
self.onmessage=async({data})=>{
 try{await ready;const query=normalizeQuery(data.query);const result=await embed(query,{pooling:'mean',normalize:true});self.postMessage({type:'results',id:data.id,query:data.query,results:semanticSearch(records,vectors,query,result.data)});}
 catch(error){self.postMessage({type:'error',id:data.id,message:String(error)});}
};
