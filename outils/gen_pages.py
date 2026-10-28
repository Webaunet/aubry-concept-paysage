import re,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(R+"/index.html",encoding="utf8").read()
hdr=re.search(r"<header.*?</header>",s,re.S).group(0)
ftr=re.search(r"<footer.*?</footer>",s,re.S).group(0)
fonts=re.search(r'<link rel="preconnect".*?<link rel="stylesheet" href="css/style.css">',s,re.S).group(0)
fav=re.search(r'<link rel="icon"[^>]*>',s).group(0)
def cur(h,p):
    h=h.replace(' aria-current="page"','')
    return h.replace(f'<a href="{p}">',f'<a href="{p}" aria-current="page">')
def img(n,alt,w,h,lazy=True):
    return f'<img src="images/{n}.jpg" width="{w}" height="{h}" {"loading=\"lazy\" " if lazy else ""}alt="{alt}">'
VAGUE='<svg class="vague" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 60V28C240 -6 480 -6 720 24S1200 58 1440 22V60z"/></svg>'
def page(f,title,desc,main):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
{fav}
{fonts}
</head>
<body>
{cur(hdr,f)}
<main>
{main}
</main>
{ftr}
<script src="js/main.js"></script>
</body>
</html>
'''
BTN2='<div class="cta-row"><a class="btn btn-terre" href="contact.html">Demander un devis</a><a class="btn btn-ligne" href="tel:+33618833051">Appeler Antoine Aubry</a></div>'
prest=f'''<section class="page-head" aria-labelledby="h1"><div class="wrap ph-grid"><div><span class="eyebrow">Prestations</span><h1 id="h1">Ce que nous aménageons chez vous</h1><p>Terrasses, allées, murets, jardins et entretien : les prestations se composent selon votre terrain et vos usages.</p>{BTN2}</div>
<div class="mosaic">{img("hero-allee-pierre","Allée en dalles de pierre bordée d'un muret et de massifs",1408,768,False)}{img("terrasse-bois","Terrasse en bois en cours de pose devant une maison en pierre",1000,545,False)}{img("jardin-contemporain","Jardin contemporain avec massifs et allée de gravier",1000,545,False)}</div></div>{VAGUE}</section>
<section class="section" id="terrasses" aria-labelledby="t1"><div class="wrap split"><div class="duo">{img("terrasse-bois","Pose d'une terrasse en bois",1000,545)}{img("allee-dallee","Chantier d'une allée dallée dans un jardin",1000,545)}</div><div><span class="eyebrow">Sols extérieurs</span><h2 id="t1">Terrasses, dallages et allées</h2><p>Un sol bien préparé et bien posé fait la durée d'un aménagement. Le revêtement se choisit selon l'usage et le style de la maison.</p><ul><li>Terrasses en bois</li><li>Dallages et allées</li><li>Cheminements entre la maison et le jardin</li></ul><a class="btn btn-terre" href="contact.html">Parler de ma terrasse</a></div></div></section>
<section class="section alt" id="maconnerie" aria-labelledby="t2"><div class="wrap split rev"><div class="duo">{img("muret-pierre","Montage d'un muret en pierre et d'un escalier de jardin",1000,545)}</div><div><span class="eyebrow">Maçonnerie paysagère</span><h2 id="t2">Murets, marches et soutènements en pierre</h2><p>La pierre structure le jardin : elle retient la terre, dessine les niveaux et donne du caractère à l'ensemble.</p><ul><li>Murets de jardin</li><li>Marches et escaliers extérieurs</li><li>Jardinières et bordures maçonnées</li></ul><a class="btn btn-terre" href="contact.html">Décrire mon projet</a></div></div></section>
<section class="section band" id="jardins" aria-labelledby="t3"><div class="wrap split"><div class="duo">{img("jardin-contemporain","Jardin contemporain en cours d'aménagement",1000,545)}{img("plantation","Plantation d'un arbuste dans un massif",1000,546)}</div><div><span class="eyebrow">Côté végétal</span><h2 id="t3">Création de jardins et plantations</h2><p>Massifs, pelouses et bordures sont dessinés ensemble, puis plantés avec des végétaux adaptés à votre terrain.</p><ul><li>Création de massifs et de pelouses</li><li>Plantation d'arbustes et de végétaux</li><li>Bordures et finitions</li></ul><a class="btn btn-clair" href="contact.html">Créer mon jardin</a></div></div></section>
<section class="section" id="entretien" aria-labelledby="t4"><div class="wrap split rev"><div class="duo">{img("taille-haie","Taille d'une haie au taille-haie",1000,747)}{img("robot-tonte","Robot de tonte sur une pelouse",1000,545)}</div><div><span class="eyebrow">Au fil des saisons</span><h2 id="t4">Entretien du jardin</h2><p>Un jardin aménagé reste beau s'il est suivi. Tonte, taille et soins se planifient selon vos besoins.</p><ul><li>Taille des haies</li><li>Tonte des pelouses</li><li>Entretien courant des massifs</li></ul><a class="btn btn-terre" href="contact.html">Organiser l'entretien</a></div></div></section>
<section class="final sol" aria-labelledby="t5"><div class="section"><div class="wrap"><span class="eyebrow">Un devis ?</span><h2 id="t5">Terrasse, allée ou jardin : décrivez-nous votre idée</h2><p>Quelques mots suffisent pour démarrer la discussion.</p><div class="cta-row"><a class="btn btn-terre" href="contact.html">Demander un devis</a><a class="btn btn-ligne" href="tel:+33618833051">06 18 83 30 51</a></div></div></div></section>'''
def ic(p):return f'<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
appr=f'''<section class="page-head" aria-labelledby="h1"><div class="wrap ph-grid"><div><span class="eyebrow">Notre approche</span><h1 id="h1">Un projet suivi de bout en bout</h1><p>Du premier échange à l'entretien, un seul interlocuteur : Antoine Aubry, dirigeant d'Aubry Concept Paysage à Orgeval.</p></div>{img("conception","Plans et préparation d'un chantier d'aménagement de jardin",1000,545,False).replace('<img','<img class="arche"')}</div>{VAGUE}</section>
<section class="section band" aria-labelledby="t1"><div class="wrap"><div class="head"><span class="eyebrow">Le déroulé</span><h2 id="t1">Du premier échange au jardin terminé</h2><p>Un projet d'aménagement avance par étapes simples, à votre rythme.</p></div>
<div class="steps"><div class="step">{ic('<circle cx="24" cy="24" r="16"/><path d="M24 14v10l7 4"/>')}<h3>Échange</h3><p>Vous présentez vos envies, vos usages et votre terrain.</p></div><div class="step">{ic('<path d="M6 38 18 10l12 28 12-18"/><path d="M6 42h36"/>')}<h3>Conception</h3><p>Le projet prend forme sur plan avant le premier coup de pelle.</p></div><div class="step">{ic('<path d="M10 40h28M14 40V26l10-10 10 10v14"/><path d="M20 40v-8h8v8"/>')}<h3>Réalisation</h3><p>Terrassement, pose, maçonnerie et plantations sur le chantier.</p></div><div class="step">{ic('<path d="M12 36c0-14 8-22 26-24-1 16-9 24-22 24"/><path d="M12 36c4-7 10-12 18-16"/>')}<h3>Entretien</h3><p>Taille, tonte et suivi pour que le jardin reste soigné.</p></div></div></div></section>
<section class="section alt" aria-labelledby="t2"><div class="wrap"><div class="head"><span class="eyebrow">Votre interlocuteur</span><h2 id="t2">Antoine Aubry, à Orgeval</h2><p>Aubry Concept Paysage est une entreprise d'aménagement paysager basée à Orgeval, dans les Yvelines. Vous échangez directement avec son dirigeant.</p></div>
<div class="engage"><div><h3>Un seul contact</h3><p>Le même interlocuteur de la demande de devis jusqu'à la fin du chantier.</p></div><div><h3>Un projet sur mesure</h3><p>Terrain, maison et usages guident chaque choix de matériaux et de végétaux.</p></div><div><h3>Une entreprise locale</h3><p>Basée à Orgeval (78), au cœur des Yvelines.</p></div></div></div></section>
<section class="final" aria-labelledby="t3"><div class="section"><div class="wrap"><span class="eyebrow">Première étape</span><h2 id="t3">Racontez-nous votre jardin</h2><p>Un appel ou un message suffit pour lancer l'échange.</p><div class="cta-row"><a class="btn btn-clair" href="contact.html">Écrire à Antoine</a><a class="btn btn-ligne" href="tel:+33618833051">Appeler</a></div></div></div></section>'''
def fld(i,l,t,ac,extra=""):return f'<div class="field"><label for="{i}">{l}</label><input id="{i}" name="{i}" type="{t}" autocomplete="{ac}" {extra} aria-describedby="err-{i}"><p class="err" id="err-{i}" role="alert"></p></div>'
cont=f'''<section class="page-head" aria-labelledby="h1"><div class="wrap"><span class="eyebrow">Contact</span><h1 id="h1">Parlons de votre projet</h1><p>Remplissez ce court formulaire : il prépare un message prêt à envoyer par SMS à Antoine Aubry.</p></div>{VAGUE}</section>
<section class="section" aria-label="Formulaire de devis"><div class="wrap"><div class="contact-grid"><div><div class="formcard"><form id="devis" novalidate>
{fld("nom","Votre nom","text","name",'required')}
{fld("tel","Votre téléphone","tel","tel",'required inputmode="tel"')}
{fld("commune","Votre commune","text","address-level2",'required')}
<div class="field"><label for="besoin">Votre besoin</label><select id="besoin" name="besoin" required aria-describedby="err-besoin"><option value="">Choisir…</option><option>Terrasse ou dallage</option><option>Allée ou muret en pierre</option><option>Création de jardin</option><option>Plantations</option><option>Entretien (tonte, taille)</option><option>Autre projet</option></select><p class="err" id="err-besoin" role="alert"></p></div>
<div class="field"><label for="message">Message <small>(facultatif)</small></label><textarea id="message" name="message" autocomplete="off"></textarea></div>
<button class="btn btn-terre" type="submit">Préparer mon message</button></form></div>
<div class="recap" id="recap" aria-live="polite"><h2>Votre message est prêt</h2><p>Rien n'est envoyé automatiquement : choisissez comment le transmettre.</p><pre id="recap-text"></pre><div class="cta-row"><a class="btn btn-terre" id="sms" href="sms:+33618833051">Envoyer par SMS</a><button class="btn btn-ligne" type="button" id="copier">Copier</button><a class="btn btn-ligne" href="tel:+33618833051">Appeler</a></div><p id="copie-ok" role="status"></p></div></div>
<aside class="side"><h2>Aubry Concept Paysage</h2><p>Antoine Aubry<br>Orgeval (78), Yvelines</p><a class="tel" href="tel:+33618833051">06 18 83 30 51</a><a class="btn btn-clair" href="tel:+33618833051">Appeler</a></aside></div></div></section>
<section class="final sol" aria-labelledby="t9"><div class="section" style="min-height:50vh"><div class="wrap"><span class="eyebrow">Plutôt par téléphone ?</span><h2 id="t9">Un appel suffit</h2><p>Antoine Aubry répond à vos questions sur votre projet d'aménagement.</p><a class="tel-big" href="tel:+33618833051">06 18 83 30 51</a></div></div></section>'''
for f,t,d,m in [("prestations.html","Prestations d'aménagement paysager à Orgeval | Aubry Concept Paysage","Terrasses, allées, murets en pierre, création de jardins, plantations et entretien : les prestations d'Aubry Concept Paysage à Orgeval (78).",prest),("approche.html","Notre approche | Aubry Concept Paysage, Orgeval","Découvrez la façon de travailler d'Aubry Concept Paysage, entreprise d'aménagement paysager à Orgeval (78), dirigée par Antoine Aubry.",appr),("contact.html","Contact et devis | Aubry Concept Paysage, Orgeval","Contactez Aubry Concept Paysage à Orgeval (78) : formulaire de devis et téléphone 06 18 83 30 51.",cont)]:
    open(R+"/"+f,"w",encoding="utf8").write(page(f,t,d,m))
print("ok")
