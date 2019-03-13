from flask import Flask, render_template
app = Flask("__name__")
@app.route("/")
def inicio():
	return render_template("inicio.html")
@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("listar_pessoas.html")
app.run()