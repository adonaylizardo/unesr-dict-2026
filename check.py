import asyncio, sys, json
from playwright.async_api import async_playwright
SIZES=[(1920,1080),(1366,768),(1440,600),(390,844)]
JS='''() => {
 const out=[]; const sl=[...document.querySelectorAll('.slide')];
 sl.forEach((s,i)=>{ window.__deck.go(i);
  const sr=s.getBoundingClientRect(); const foot=s.querySelector('.foot'); const fr=foot?foot.getBoundingClientRect():null;
  const probs=[];
  s.querySelectorAll('.body *').forEach(el=>{
    if(el.closest('.glow,.notes')||el.closest('.cover .win')||el.matches('.gif')) return;
    const r=el.getBoundingClientRect(); if(!r.width||!r.height) return;
    const st=getComputedStyle(el); if(st.display==='none'||st.visibility==='hidden') return;
    if(r.right>sr.right+1||r.left<sr.left-1||r.bottom>sr.bottom+1||r.top<sr.top-1) probs.push('out:'+el.className+':'+(el.textContent||'').trim().slice(0,30));
    if(fr && (el.children.length===0 && el.textContent.trim() || el.matches('.step,.card,.ck,.cal,.agenda,.placeholder,.flow,.grid')) && r.bottom>fr.top-4 && r.top<fr.bottom) probs.push('foot:'+(el.textContent||'').trim().slice(0,30));
    const box=el.parentElement && el.parentElement.closest('.ck,.card,.step,.cal,.win,.agenda,.placeholder,.blk');
    if(box){const b=box.getBoundingClientRect(); if(r.bottom>b.bottom+1||r.right>b.right+1) probs.push('inbox:'+el.className+':'+(el.textContent||'').trim().slice(0,30));}
    if(el.scrollWidth>el.clientWidth+2 && st.overflow!=='visible' && el.clientWidth) probs.push('clip:'+el.className);
  });
  if(foot){const kids=[...foot.querySelectorAll('.ev,.lg,.n')].filter(e=>getComputedStyle(e).display!=='none').map(e=>[e,e.getBoundingClientRect()]);
    kids.forEach(([e,r])=>{ if(r.right>sr.right+1||r.left<sr.left-1||r.bottom>sr.bottom+1) probs.push('footout:'+e.className);
      kids.forEach(([e2,r2])=>{ if(e!==e2 && !(r.right<=r2.left||r2.right<=r.left||r.bottom<=r2.top||r2.bottom<=r.top)) probs.push('footlap:'+e.className+'/'+e2.className);});});}
  if(probs.length) out.push({slide:i+1,probs:[...new Set(probs)].slice(0,6)});
 }); return out; }'''
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for w,h in SIZES:
      pg=await b.new_page(viewport={'width':w,'height':h})
      await pg.goto('http://127.0.0.1:32997/index.html#1'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
      r=await pg.evaluate(JS)
      print(f'== {w}x{h}: {len(r)} slides with issues'); 
      for x in r: print(' ',x)
      await pg.close()
    await b.close()
asyncio.run(main())
