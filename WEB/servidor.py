from flask import Flask, render_template, request, redirect, session
from hashlib import md5
import peewee_site as p

app = Flask(__name__)
app.secret_key = 'senha'

m = md5()
logado = False
pegar = lambda x: request.args.get(x)
cor_bg = "#FFFFFF"

p.db.connect()
try:
	p.db.create_tables([p.Pessoa, p.Contas])
except:
	print("erro ao criar tabelas")

@app.route("/")
def inicio():
	global logado
	return render_template("inicio.html", logado = logado, cor_bg = cor_bg)
	
@app.route("/noturno")
def noturno():
	global cor_bg
	if cor_bg == "#FFFFFF":
		cor_bg = "#202020"
	else:
		cor_bg = "#FFFFFF"
	return redirect(())

@app.route("/listar_pessoas")
def listar_pessoas():
	global cor_bg
	return render_template("listar_pessoas.html", users = p.Pessoa.select(), logado = logado, cor_bg = cor_bg)

@app.route("/ver_video")
def ver_video():
	return render_template("ver_video.html")

@app.route("/form_adicionar")
def form_adicionar():
	return render_template("form_adicionar.html")

@app.route("/adicionar_pessoa")
def adicionar_pessoa():
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	p.Pessoa.create(nom_pessoa = nome, endereco = endereco)
	return redirect("/listar_pessoas")

@app.route("/deletar_pessoa")
def deletar_pessoa():
	cod = request.args.get("cod_pessoa")
	p.Pessoa.delete_by_id(cod)
	return redirect("/listar_pessoas")

@app.route("/form_alterar")
def form_alterar():
	cod_pessoa = request.args.get("cod_pessoa")
	nom_pessoa = request.args.get("nom_pessoa")
	ende = request.args.get("endereco")
	return render_template("form_alterar.html", cod_pessoa = cod_pessoa, nom_pessoa = nom_pessoa, endereco = ende)

@app.route("/alterar_pessoa")
def alterar_pessoa():
	cod_pessoa = pegar("cod_pessoa")
	nome = pegar("nom_pessoa")
	ende = pegar("endereco")
	pe = p.Pessoa.get_by_id(cod_pessoa)
	pe.nom_pessoa = nome
	pe.endereco = ende
	pe.save()
	return redirect("/listar_pessoas")

@app.route("/form_login")
def form_login():
	try:
		if session["user"]:
			redirect("/")
	except:
		return render_template("form_login.html")


@app.route("/login", methods = ["POST"])
def login():
	global m
	global logado
	if logado:
		pass
	else:
		user = request.form["user"]
		senha_comparar = p.Contas.select().where(p.Contas.user == user)
		m.update(request.form["passwd"].encode())
		senha = m.hexdigest()
		if senha == senha_comparar[0].passwd:
			logado = True
			m = md5()
			session["user"] = user
	return redirect("/")

@app.route("/form_cadastrar")
def form_cadastrar():
	return render_template("form_cadastrar.html")
		
@app.route("/cadastrar_user", methods = ["POST"])
def cadastrar_user():
	user = request.form['user']
	senha = request.form['passwd'].encode()
	print(senha)
	m.update(senha)
	senha = m.hexdigest()
	print(user)
	print(senha)
	p.Contas.create(user = user, passwd = senha)
	return redirect("/")

		
@app.route("/logout")
def logout():
	global logado
	logado = False
	return redirect("/")


app.run(debug=True)