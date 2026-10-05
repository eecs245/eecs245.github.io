import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {parseHTML} from 'linkedom';
import {buildSearch,indexedCoverage} from '../public/search.mjs';
import {createHybridSearch} from '../public/hybrid.mjs';
import {parseResourceQuery} from '../public/resource-query.mjs';

test('video results have direct links and their category can be toggled',async()=>{
 const {window,document}=parseHTML(await readFile(new URL('../public/index.html',import.meta.url),'utf8'));
 const title='Why is rank(X^TX) = rank(X)?',url='https://www.youtube.com/watch?v=hOyaHqGmO1I';
 const records=[{id:'video',category:'Other videos',title,section:'Watch video',text:title,url,concepts:[],detail:'Video title'}];
 let worker;
 Object.assign(globalThis,{window,document,parent:{postMessage(){}},location:{search:'',origin:'http://localhost'},
  Worker:class {constructor(){worker=this;}postMessage(message){if(message.query)this.request=message;}},
  fetch:async()=>({ok:true,json:async()=>({records})})});
 await import('../public/app.js');
 document.querySelector('#search').value='rank';
 document.querySelector('#search-form').dispatchEvent(new window.Event('submit',{cancelable:true}));
 worker.onmessage({data:{type:'ready'}});
 worker.onmessage({data:{type:'results',...worker.request,results:buildSearch(records)(worker.request.query)}});
 const group=()=>document.querySelector('.group[data-category="Other videos"]');
 assert.equal(group().querySelector('h3 a').textContent,title);
 assert.equal(group().querySelector('h3 a').getAttribute('href'),url);
 assert.equal(group().querySelector('.locations a').textContent,'Watch video');
 assert.equal(group().querySelector('details'),null);
 assert.match(document.querySelector('#index-coverage').textContent,/Other videos: 1/);
 const filter=document.querySelector('button[data-category="Other videos"]');
 assert.equal(filter.getAttribute('aria-pressed'),'true');
 filter.click();assert.equal(group(),null);
 filter.click();assert.equal(group().querySelector('h3 a').getAttribute('href'),url);
});

test('exam navigation retrieves the matching walkthrough without leaking other videos',()=>{
 const record=(id,category,title,section)=>({id,category,title,section,text:title,url:`https://example.org/${id}`,concepts:[],detail:''});
 const records=[
  record('exam','Past exams','Fall 2025 Midterm 1','Problem 5: Back to Normal'),
  record('video','Other videos','Fall 2025 Midterm 1 Problem 5 – EECS 245','Watch video'),
  record('other','Other videos','Fall 2025 Midterm 1 Problem 6 – EECS 245','Watch video'),
  record('term','Other videos','Winter 2026 Midterm 1 Problem 5 – EECS 245','Watch video'),
  record('concept','Other videos','Overview: Projecting onto the column space','Watch video')];
 const search=createHybridSearch(records,new Float32Array(records.length*384));
 assert.deepEqual(search(parseResourceQuery('Fall 2025 Midterm 1 problem 5')).map(r=>r.title),records.slice(0,2).map(r=>r.title));
 assert.equal(search(parseResourceQuery('HW 5 problem 5')).length,0);
 assert.equal(indexedCoverage([records[1],records[1]]).match(/Other videos: (\d+)/)[1],'1');
});
