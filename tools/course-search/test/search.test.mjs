import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {buildSearch,categories,groupDocuments} from '../public/search.mjs';
const records=JSON.parse(readFileSync(new URL('../search-index.json',import.meta.url))).records;
const search=buildSearch(records);
test('projection groups documents once while retaining their matching section links',()=>{
 const results=search('projection');
 assert(categories.every(category=>results.some(r=>r.category===category)));
 assert.equal(new Set(results.map(r=>r.url)).size,results.length);
 assert(results.some(r=>r.locations.some(location=>location.url.endsWith('#orthogonal-projections'))));
 const note=results.find(r=>r.url.endsWith('/projecting-onto-a-single-vector/'));
 assert(note.locations.length>1);
 assert.equal(new Set(note.locations.map(location=>location.url)).size,note.locations.length);
});
test('topic aliases work and unknown terms produce no matches',()=>{
 assert.deepEqual(search('proj').map(r=>r.id),search('projection').map(r=>r.id));
 assert.equal(search('zzzznothingmatches').length,0);
});
test('document title alone cannot create an irrelevant problem card',()=>{
 const query=buildSearch([{id:'1',category:'Homeworks',title:'Projections homework',section:'Problem 1',text:'Review your earlier work',url:'https://eecs245.org/example'}]);
 assert.equal(query('projection').length,0);
});

test('document grouping keeps the best chunk for each location and each PDF page',()=>{
 const results=groupDocuments([
 {id:'1',category:'Notes',title:'Note',url:'https://example.com/note/#a',section:'A',text:'best',score:10},
 {id:'2',category:'Notes',title:'Note',url:'https://example.com/note/#a',section:'A',text:'duplicate',score:5},
 {id:'3',category:'Notes',title:'Note',url:'https://example.com/note/#b',section:'B',text:'other',score:3},
 {id:'4',category:'Lecture PDFs',title:'Lecture',url:'https://example.com/lecture.pdf#page=2',section:'Page 2',score:2},
 {id:'5',category:'Lecture PDFs',title:'Lecture',url:'https://example.com/lecture.pdf#page=3',section:'Page 3',score:1}
 ]);
 assert.equal(results.length,2);assert.equal(results[0].locations.length,2);assert.equal(results[0].locations[0].text,'best');assert.equal(results[1].locations.length,2);
});

test('code vocabulary cannot collide with inherited object properties',()=>{
 const s=buildSearch([{id:'1',category:'Notes',title:'Code',section:'Constructor',text:'constructor prototype objects',url:'https://example.com/code'}]);
 assert.equal(s('constructor').length,1);
});

test('sorting uses score or numeric course order without mutating results',async()=>{
 const {sortDocuments}=await import('../public/search.mjs');
 const notes=[{title:'3.10. Later',category:'Notes',score:9},{title:'3.2. Earlier',category:'Notes',score:1}];
 assert.equal(sortDocuments(notes,'chronological')[0].title,'3.2. Earlier');
 assert.equal(sortDocuments(notes,'relevance')[0].score,9);
 const exams=[{title:'Winter 2026 Midterm 1',category:'Past exams',score:5},{title:'Fall 2025 Final Exam',category:'Past exams',score:1},{title:'Fall 2025 Midterm 2',category:'Past exams',score:2}];
 assert.deepEqual(sortDocuments(exams,'chronological').map(r=>r.title),['Fall 2025 Midterm 2','Fall 2025 Final Exam','Winter 2026 Midterm 1']);
 assert.equal(exams[0].title,'Winter 2026 Midterm 1');
});
test('excluded notebooks, lab recaps, and practice exams never enter the index',()=>{
 assert(records.every(r=>!r.url.includes('github.com/eecs245/fa26-code')));
 assert(records.every(r=>r.category!=='Labs'||!/^Recap\b/i.test(r.section)));
 assert(records.every(r=>r.category!=='Past exams'||!/practice|mock/i.test(r.title+' '+r.url)));
});
