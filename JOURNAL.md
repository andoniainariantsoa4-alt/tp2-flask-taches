#Journal de découverte
## Mission 1 - Faire tourner Flask 
- Essayé : python app.py
- Observé : serveur sur 127.0.0.1:5000, WARNING developpement server, rechargement auto quand je modifie app.py
- Doc : Flask Quikstart > une application Minimakle, Debug Mode
- Expliqué : app.run(debug=True)  a activé le reloader qui a pour mission de surveiller les fichiers et le debugger dans le navigateur. Le WARNING est normal.

## Mission 2 - Listes de tâches
- Ajout liste 'tâches' dans app.py (3 dictionnaires)
- Création templates/taches.html avec boucle for

## Mission 3 - Listes de tâches 
Mission 4 : erreur endlock -> endlock corrigée
- Route /tachs/<int:id>
- Erreur rencontrée :  '{{{ t.priorite }}}' -> TemplateSyntaxError expected token ':'
- Correction:  instead of three "{}",  i change it to "()"
- Test 404 : /taches/99 renvoie bien 404

## Mission 4 : Héritage base.html
- Création templates/base.htmlavec nav + block content
- Création templates/detail.html qui extends base.html
- Modification taches.html pour extendsbase.html
- Erreur rencontrée : '{% endlock %}au lieu de '(% endblock %)'
- Correction :  renommer en endblock ligne 13 de base.html
- Réseau : menu comun Accueil vixible sur / et /taches/2

## Mission 5 : Formulaire d'ajout
- Route /nouvelle GET + POST avec request.form
- Erreurs rencontrées :
    1. Adress already in use Port 5000 -> lsof -ti:5000 | xargs kill -9
    2. Nameerror nouveau_id is not defined -> cause '==' au lie de '=' dans la ligne 25 de app.py
- test : ajout "acheter du pain" O, redirection vers / avec 4 tâches
