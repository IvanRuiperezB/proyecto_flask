from flask import Flask, render_template, abort, request
import json
app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template("inicio.html")
@app.route('/recetas')
def recetas():
    return render_template("recetas.html")
@app.route('/listarecetas', methods=["POST"])
def listarecetas():
    receta=request.form.get("receta")
    return render_template("listarecetas.html",receta=receta)
app.run("0.0.0.0",5000,debug=True)