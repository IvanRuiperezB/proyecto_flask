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
    with open("Data_Recipes.json") as fich:
        datos=json.load(fich)
    recetas=[]
    for item in datos:
        if receta.lower() in item["name"].lower():
            if item["name"] not in recetas:
                receta1={"name":item["name"],"autor":item["author"],"detalles":item["_id"]["$oid"]}
                recetas.append(receta1)
    return render_template("listarecetas.html",recetas=recetas)
app.run("0.0.0.0",5000,debug=True)