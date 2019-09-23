from flask import Flask, render_template, request, redirect, session
import peewee_site as p
import requests
app = Flask("__name__")
app.secret_key = 'senha'

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/form_signin")
def form_signin():

	return render_template("form_signin.html")

@app.route("/signin", methods = ["POST"])
def signin():
	user = request.form["user"]
	passwd = request.form["passwd"]
	name = request.form["name"]

	cadastrado = requests.get("localhost:4999/cadastrar_usuario?user="+user+"&passwd="+passwd+"&name="+name)
	if cadastrado:
		return "Cadastrado <br> <a href='/'>Voltar</a>"
	else:
		return "Erro ao cadastrar <br> <a href='/form_signin'>Voltar</a>"