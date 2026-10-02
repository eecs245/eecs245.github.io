(() => {
 const trigger=document.querySelector('.smart-search-trigger');if(!trigger)return;
 const modal=document.createElement('dialog');modal.className='smart-search-modal';modal.setAttribute('aria-label','Smart Search');
 const close=document.createElement('button');close.type='button';close.className='smart-search-close';close.textContent='×';close.setAttribute('aria-label','Close Smart Search');
 const frame=document.createElement('iframe');frame.title='Search EECS 245 course materials';frame.className='smart-search-frame';
 modal.append(close,frame);document.body.append(modal);
 let returnFocus;
 const focusSearch=()=>frame.contentWindow?.postMessage({type:'eecs245-search-focus'},location.origin);
 function open(){returnFocus=document.activeElement;if(!frame.src)frame.src=trigger.dataset.searchUrl;if(!modal.open){modal.showModal();document.body.classList.add('smart-search-open');}focusSearch();}
 function dismiss(){if(modal.open)modal.close();}
 close.addEventListener('click',dismiss);trigger.addEventListener('click',open);
 frame.addEventListener('load',focusSearch);
 modal.addEventListener('click',event=>{if(event.target===modal){const r=modal.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dismiss();}});
 modal.addEventListener('close',()=>{document.body.classList.remove('smart-search-open');returnFocus?.focus();});
 document.addEventListener('keydown',event=>{if((event.metaKey||event.ctrlKey)&&event.key.toLowerCase()==='f'){event.preventDefault();open();}});
 window.addEventListener('message',event=>{if(event.origin!==location.origin||event.source!==frame.contentWindow)return;if(event.data?.type==='eecs245-search-close')dismiss();if(event.data?.type==='eecs245-search-focus-parent')open();});
})();
