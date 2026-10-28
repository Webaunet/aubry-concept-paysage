(function(){
  var b=document.querySelector('.burger'),n=document.getElementById('menu');
  if(!b||!n)return;
  function set(o){b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu');n.classList.toggle('open',o)}
  b.addEventListener('click',function(){set(b.getAttribute('aria-expanded')!=='true')});
  n.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&n.classList.contains('open')){set(false);b.focus()}});
  window.matchMedia('(min-width:981px)').addEventListener('change',function(){set(false)});
})();
(function(){
  var f=document.getElementById('devis');if(!f)return;
  var R=document.getElementById('recap'),T=document.getElementById('recap-text');
  var rules={nom:function(v){return v.trim().length>=2||'Indiquez votre nom.'},
    tel:function(v){return /^(?:\+33|0033|0)[1-9](?:[\s.\-]?\d{2}){4}$/.test(v.trim())||'Indiquez un numéro valide, par exemple 06 12 34 56 78.'},
    commune:function(v){return v.trim().length>=2||'Indiquez votre commune.'},
    besoin:function(v){return v!==''||'Choisissez votre besoin.'}};
  function check(id){var el=document.getElementById(id),r=rules[id](el.value),box=el.closest('.field'),e=document.getElementById('err-'+id);
    if(r===true){box.removeAttribute('data-bad');el.removeAttribute('aria-invalid');e.textContent='';return true}
    box.setAttribute('data-bad','');el.setAttribute('aria-invalid','true');e.textContent=r;return false}
  Object.keys(rules).forEach(function(id){document.getElementById(id).addEventListener('blur',function(){check(id)})});
  f.addEventListener('submit',function(ev){ev.preventDefault();
    var first=null;Object.keys(rules).forEach(function(id){if(!check(id)&&!first)first=id});
    if(first){document.getElementById(first).focus();return}
    var g=function(i){return document.getElementById(i).value.trim()};
    var txt='Bonjour, je souhaite un devis.\nNom : '+g('nom')+'\nTéléphone : '+g('tel')+'\nCommune : '+g('commune')+'\nBesoin : '+g('besoin')+(g('message')?'\nMessage : '+g('message'):'');
    T.textContent=txt;document.getElementById('sms').href='sms:+33618833051?&body='+encodeURIComponent(txt);
    R.classList.add('show');R.setAttribute('tabindex','-1');R.focus();R.scrollIntoView({behavior:'smooth',block:'start'})});
  var cp=document.getElementById('copier'),ok=document.getElementById('copie-ok');
  cp.addEventListener('click',function(){var t=T.textContent;
    function done(){ok.textContent='Texte copié.'}
    function fb(){var r=document.createRange();r.selectNodeContents(T);var s=getSelection();s.removeAllRanges();s.addRange(r);ok.textContent='Texte sélectionné : copiez-le avec Ctrl+C.'}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(done,fb)}else fb()});
})();
