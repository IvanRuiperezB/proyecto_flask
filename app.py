from flask import Flask, render_template, abort, request
import json
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/recetas', methods=["POST","GET"])
def recetas():
    with open("Data_Recipes.json") as fich:
            datos=json.load(fich)
    autores=[]
    for dato in datos:
        if dato["author"] not in autores:
            autores.append(dato["author"])
    if request.method=="GET":
        recetas=1
        return render_template("recetas.html",recetas=recetas,autores=autores)
    else:
        receta=request.form.get("receta")
        seleccionado=request.form.get("autores")
        recetas=[]
        for item in datos:
            if receta.lower() in item["name"].lower() and seleccionado in item["author"]:
                if item["name"] not in recetas:
                    receta1={"name":item["name"],"autor":item["author"],"detalles":item["_id"]["$oid"]}
                    recetas.append(receta1)
        if len(recetas) == 0:
            recetas=0
        autores=[]
        for dato in datos:
            if dato["author"] not in autores:
                autores.append(dato["author"])
        return render_template("recetas.html",receta=receta,recetas=recetas,autores=autores,seleccionado=seleccionado)

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
    if len(recetas) == 0:
        recetas=0
    return render_template("listarecetas.html",recetas=recetas)

@app.route('/receta')
def receta():
    id=request.args.get("id")
    with open("Data_Recipes.json") as fich:
        datos=json.load(fich)
    recetas={}
    ingredientes=[]
    pasos=[]
    for receta in datos:
        if receta["_id"]["$oid"] == id:
            recetas={"name":receta["name"],"autor":receta["author"],"desc":receta["description"],"prep":receta["preparation_time"],"cocina":receta["cook_time"],"comensales":receta["servings"]}
            for ingrediente in receta["ingredients"]:
                ing=ingrediente["qty"]+" "+ingrediente["name"]
                ingredientes.append(ing)
            if len(receta["instructions"]) > 1:
                for paso in receta["instructions"]:
                    pasos.append(paso["detail"])
            else:
                pasos=0
            return render_template("receta.html",recetas=recetas,ingredientes=ingredientes,pasos=pasos)
    return abort(404)

port=os.environ["PORT"]
app.run("0.0.0.0", int(port),debug=False)