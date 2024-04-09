from flask import Flask, render_template, abort
app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template("inicio.html")
@app.route('/recetas')
def recetas():
    return render_template("recetas.html")

app.run("0.0.0.0",5000,debug=True)