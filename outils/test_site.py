import sys,os,re,glob
from playwright.sync_api import sync_playwright
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages=sorted(glob.glob(R+"/*.html"))
W=[int(a) for a in sys.argv[1:]] or [390,768,1280]
bad=[]
JS="""()=>{const o=[],vw=innerWidth;
if(document.documentElement.scrollWidth>vw)o.push('debordement-h '+document.documentElement.scrollWidth);
document.querySelectorAll('p,li,a,span,h1,h2,h3,label,button,small,b').forEach(e=>{if(!e.offsetParent)return;const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());if(!t)return;const s=parseFloat(getComputedStyle(e).fontSize);if(s<(vw<600?16:14.9))o.push('texte '+s+' '+e.textContent.trim().slice(0,20))});
document.querySelectorAll('a,button').forEach(e=>{if(!e.offsetParent)return;const r=e.getBoundingClientRect();if(r.height<44||r.width<44)o.push('cible '+Math.round(r.width)+'x'+Math.round(r.height)+' '+(e.textContent.trim().slice(0,18)||e.className))});
document.querySelectorAll('section').forEach(s=>{const h=s.getBoundingClientRect().height/innerHeight;if(h>1.45)o.push('section haute '+h.toFixed(2)+' '+(s.getAttribute('aria-labelledby')||''))});
const f=document.querySelector('footer');if(f&&f.getBoundingClientRect().height>innerHeight*.3)o.push('footer haut');
document.querySelectorAll('img').forEach(i=>{if(i.complete&&i.naturalWidth==0)o.push('img cassée '+i.src)});
return o}"""
with sync_playwright() as p:
    b=p.chromium.launch()
    for pg in pages:
        txt=open(pg,encoding="utf8").read()
        for l in re.findall(r'(?:href|src)="(?!https?:|tel:|mailto:|sms:|#|data:)([^"#?]+)',txt):
            if not os.path.exists(os.path.join(R,l)):bad.append(f"{os.path.basename(pg)} lien {l}")
        for w in W:
            c=b.new_page(viewport={"width":w,"height":900 if w>600 else 800});c.goto("file://"+pg);c.wait_for_timeout(300)
            for m in c.evaluate(JS):bad.append(f"{os.path.basename(pg)}@{w} {m}")
            c.close()
    b.close()
for f in glob.glob(R+"/images/*"):
    if os.path.getsize(f)>250000:bad.append("poids "+f)
print("\n".join(sorted(set(bad))) or "TOUT OK")
