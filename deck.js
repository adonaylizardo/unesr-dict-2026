(function(){
  var root=document.documentElement, stage=document.getElementById('stage');
  var slides=[].slice.call(document.querySelectorAll('.slide'));
  var N=slides.length, cur=0;
  var label=(document.body.getAttribute('data-foot')||'').replace(/^Adonay Lizardo/,'<b>Adonay Lizardo</b>');
  function logos(){return '<span class="logos">'+
    '<span class="sinlock"><img class="lg lg-sin" src="logos/sinergia.png" alt=""><span class="sinw">Sinergia</span></span>'+
    '<span class="lg-x">×</span>'+
    '<img class="lg lg-sxai" src="logos/spacexai.png" alt="SpaceXAI">'+
    '</span>';}
  slides.forEach(function(s,i){
    if(s.hasAttribute('data-nofoot'))return;
    var f=document.createElement('div');f.className='foot'+(s.getAttribute('data-foot')==='hero'?' hero':'');
    f.innerHTML=logos()+'<span class="ev">'+label+'</span><span class="n">'+(i+1)+' / '+N+'</span>';
    s.appendChild(f);
  });
  function fit(){
    var vw=window.innerWidth, vh=window.innerHeight, cw=1920, ch=1080;
    var portrait = vw/vh < 0.8;
    root.classList.toggle('portrait',portrait);
    if(portrait){cw=1080;ch=Math.round(Math.min(2400,Math.max(1600,1080*vh/vw)));}
    var s=Math.min(vw/cw,vh/ch);
    root.style.setProperty('--cw',cw+'px');root.style.setProperty('--ch',ch+'px');root.style.setProperty('--s',s);
  }
  function go(i,push){
    cur=Math.max(0,Math.min(N-1,i));
    slides.forEach(function(s,k){s.classList.toggle('on',k===cur)});
    var h='#'+(cur+1); if(location.hash!==h)history.replaceState(null,'',h);
    var g=document.querySelectorAll('#grid a');[].forEach.call(g,function(a,k){a.classList.toggle('cur',k===cur)});
  }
  function fromHash(){var n=parseInt(location.hash.slice(1),10);go(isNaN(n)?0:n-1)}
  // overview
  var grid=document.getElementById('grid');
  slides.forEach(function(s,i){var a=document.createElement('a');a.href='#'+(i+1);
    a.innerHTML='<span>'+(i+1)+'</span>'+(s.getAttribute('data-title')||'');
    a.onclick=function(e){e.preventDefault();go(i);grid.classList.remove('on')};grid.appendChild(a)});
  document.addEventListener('keydown',function(e){
    if(/input|textarea/i.test(e.target.tagName))return;
    var k=e.key;
    if(k==='ArrowRight'||k==='ArrowDown'||k==='PageDown'||(k===' '&&!e.shiftKey)){e.preventDefault();go(cur+1)}
    else if(k==='ArrowLeft'||k==='ArrowUp'||k==='PageUp'||(k===' '&&e.shiftKey)){e.preventDefault();go(cur-1)}
    else if(k==='Home')go(0);else if(k==='End')go(N-1);
    else if(k==='f'||k==='F'){if(!document.fullscreenElement)root.requestFullscreen&&root.requestFullscreen();else document.exitFullscreen()}
    else if(k==='b'||k==='B'||k==='.'){var b=document.getElementById('black');b.style.display=b.style.display==='block'?'none':'block'}
    else if(k==='g'||k==='G'){grid.classList.toggle('on')}
    else if(k==='Escape'){grid.classList.remove('on')}
    else if(k==='n'||k==='N'){var n=slides[cur].querySelector('.notes');if(n)console.log('Notas '+(cur+1)+': '+n.textContent.trim())}
  });
  document.getElementById('nav-l').onclick=function(){go(cur-1)};
  document.getElementById('nav-r').onclick=function(){go(cur+1)};
  var tx=null,ty=null;
  window.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;ty=e.touches[0].clientY},{passive:true});
  window.addEventListener('touchend',function(e){if(tx===null)return;var dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;
    if(Math.abs(dx)>50&&Math.abs(dx)>Math.abs(dy))go(cur+(dx<0?1:-1));tx=null},{passive:true});
  window.addEventListener('resize',fit);window.addEventListener('hashchange',fromHash);
  fit();fromHash();
  window.__deck={go:go,N:N,slides:slides};
})();
