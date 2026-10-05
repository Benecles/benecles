/* A shared spring preview for interactive lists. No click handling or reading-content movement. */
(function(){
  var reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
  var groups=[
    {list:'.reg-rows',target:'.reg-row[href]',speed:'moderate'},
    {list:'.dialogues',target:'a',speed:'moderate'},
    {list:'.quiz,.retrieval-quiz',target:'details',speed:'slow'},
    {list:'.bet-opts',target:'button',speed:'fast'},
    {list:'.endnav',target:'a',speed:'fast'}
  ];
  var selector=groups.map(function(g){return g.list}).join(',');
  document.querySelectorAll(selector).forEach(function(list){
    var spec=groups.find(function(g){return list.matches(g.list)});
    var targets=Array.prototype.slice.call(list.querySelectorAll(spec.target));
    if(!targets.length)return;
    list.setAttribute('data-motion-list','');list.setAttribute('data-motion-speed',spec.speed);
    var slab=document.createElement(list.matches('.reg-rows,.dialogues')?'li':'span');slab.setAttribute('data-motion-slab','');slab.setAttribute('aria-hidden','true');list.insertBefore(slab,list.firstChild);
    targets.forEach(function(t){t.setAttribute('data-motion-target','')});
    var x=0,y=0,sx=0,sy=0,tx=0,ty=0,tsx=0,tsy=0,opacity=0,toOpacity=0,vx=0,vy=0,vsx=0,vsy=0,vo=0,raf=0,last=0,active=null;
    function box(target){
      var members=[target],key=target.getAttribute('data-motion-group');
      if(key)members=targets.filter(function(other){return other.getAttribute('data-motion-group')===key});
      var a=Infinity,b=Infinity,c=-Infinity,d=-Infinity;
      members.forEach(function(el){var r=el.getBoundingClientRect();a=Math.min(a,r.left);b=Math.min(b,r.top);c=Math.max(c,r.right);d=Math.max(d,r.bottom)});
      var root=list.getBoundingClientRect();return [a-root.left,b-root.top,c-a,d-b];
    }
    function aim(target){
      if(!target){active=null;toOpacity=0;targets.forEach(function(t){t.removeAttribute('data-motion-active')});if(reduced.matches){opacity=0;slab.style.opacity='0'}return}
      active=target;targets.forEach(function(t){if(!reduced.matches&&(t===target||target.getAttribute('data-motion-group')&&t.getAttribute('data-motion-group')===target.getAttribute('data-motion-group')))t.setAttribute('data-motion-active','');else t.removeAttribute('data-motion-active')});
      var b=box(target);tx=b[0];ty=b[1];tsx=b[2];tsy=b[3];toOpacity=1;
      if(reduced.matches){x=tx;y=ty;sx=tsx;sy=tsy;opacity=1;paint()}
      else if(!raf){last=performance.now();raf=requestAnimationFrame(step)}
    }
    function paint(){slab.style.transform='translate3d('+x+'px,'+y+'px,0) scale('+sx+','+sy+')';slab.style.opacity=String(opacity)}
    function step(now){
      var dt=Math.min(.032,Math.max(.001,(now-last)/1000));last=now;
      var k=Number(getComputedStyle(slab).getPropertyValue('--motion-k'))||560,damper=2*Math.sqrt(k)*.84;
      function spring(p,v,dest){var acc=k*(dest-p)-damper*v;v+=acc*dt;p+=v*dt;return [p,v]}
      var q=spring(x,vx,tx);x=q[0];vx=q[1];q=spring(y,vy,ty);y=q[0];vy=q[1];q=spring(sx,vsx,tsx);sx=q[0];vsx=q[1];q=spring(sy,vsy,tsy);sy=q[0];vsy=q[1];q=spring(opacity,vo,toOpacity);opacity=q[0];vo=q[1];paint();
      if(Math.abs(tx-x)+Math.abs(ty-y)+Math.abs(tsx-sx)+Math.abs(tsy-sy)+Math.abs(toOpacity-opacity)<.12&&Math.abs(vx)+Math.abs(vy)+Math.abs(vsx)+Math.abs(vsy)+Math.abs(vo)<1.4){x=tx;y=ty;sx=tsx;sy=tsy;opacity=toOpacity;paint();raf=0;return}
      raf=requestAnimationFrame(step)
    }
    list.addEventListener('pointerover',function(e){if(e.pointerType==='touch')return;var t=e.target.closest('[data-motion-target]');if(t&&list.contains(t)&&t!==active)aim(t)});
    list.addEventListener('pointerleave',function(e){if(e.pointerType!=='touch')aim(null)});
    list.addEventListener('focusin',function(e){var t=e.target.closest('[data-motion-target]');if(t&&list.contains(t))aim(t)});
    list.addEventListener('focusout',function(){requestAnimationFrame(function(){if(!list.contains(document.activeElement))aim(null)})});
    if(reduced.addEventListener)reduced.addEventListener('change',function(e){if(e.matches){if(raf)cancelAnimationFrame(raf);raf=0;if(active)aim(active);else{opacity=0;toOpacity=0;paint()}}});
    window.addEventListener('resize',function(){if(active)aim(active)},{passive:true});
    window.addEventListener('scroll',function(){if(active)aim(active)},{passive:true,capture:true});
  });
})();
