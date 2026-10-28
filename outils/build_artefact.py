import re,base64,os,sys
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(R+"/index.html",encoding="utf8").read()
css=open(R+"/css/style.css",encoding="utf8").read()
css=css.replace("@media (prefers-color-scheme:dark){\n  :root{","@media (prefers-color-scheme:dark){\n  :root:not([data-theme=\"light\"]){")
dk=re.search(r':root:not\(\[data-theme="light"\]\)\{(.*?)\}\n\}',css,re.S).group(1)
css+=f'\n:root[data-theme="dark"]{{{dk}}}\n'
js=open(R+"/js/main.js",encoding="utf8").read()
head=re.search(r"<title>.*?</title>",s,re.S).group(0)
fonts=re.search(r'<link rel="stylesheet" href="https://fonts[^>]*>',s).group(0)
body=re.search(r"<body>(.*?)<script src",s,re.S).group(1)
body=body.replace("approche.html","#apropos").replace("prestations.html","#prestations").replace("contact.html","#contact").replace('href="index.html"','href="#top"')
body=body.replace('<section class="section" aria-labelledby="t-about">','<section class="section" id="apropos" aria-labelledby="t-about">').replace('<section class="final"','<section class="final" id="contact"').replace('<header class="site-header">','<header class="site-header" id="top">')
def b64(m):
    p=R+"/"+m.group(1);return 'src="data:image/jpeg;base64,'+base64.b64encode(open(p,"rb").read()).decode()+'"'
body=re.sub(r'src="(images/[^"]+)"',b64,body)
out=f"{head}\n{fonts}\n<style>{css}</style>\n{body}\n<script>{js}</script>\n"
open(sys.argv[1],"w",encoding="utf8").write(out);print(len(out)//1024,"Ko")
