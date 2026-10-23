from flask import Flask, abort, render_template, request, redirect, url_for

app = Flask(__name__)

taches = [
    {"id": 1, "titre": "Réviser les décorateurs", "priorite": "haute", "terminee": False},
    {"id": 2, "titre": "Installer Flask", "priorite": "normale", "terminee": True},
    {"id": 3, "titre": "lire la doc Jinja2", "prorite": "basse", "terminee": False}, 
]

@app.route('/')
def index():
    return render_template("taches.html", taches=taches)

@app.route("/taches/<int:id>")
def detail(id):
    for t in taches:
        if t["id"] == id:
            return render_template("detail.html", tache=t)
    abort(404)

@app.route("/nouvelle", methods=["GET", "POST"])
def nouvelle():
    if request.method == "POST":
        nouveau_id = max(t["id"] for t in taches) + 1 if taches else 1
        titre = request.form.get("titre")
        priorite = request.form.get("priorite", "normale")
        if titre: 
            taches.append({"id": nouveau_id, "titre": titre, "priorite": priorite, "terminee": False})
        return redirect(url_for("index"))
    return render_template("nouvelle.html")

if __name__ == "__main__":
    app.run(debug=True)

    