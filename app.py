from flask import Flask, abort, render_template

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
            return render_template("taches.html", taches=[t])
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)

    