from flask import Flask, render_template, request, redirect, session
from hashlib import md5
import peewee_site as p

app = Flask("__name__")
app.secret_key = 'senha'
m = md5()
logado = False
pegar = lambda x: request.args.get(x)
pegar2 = lambda x: request.form[x]

p.db.connect()
try:
	p.db.create_tables([p.Pessoa, p.Contas])
except:
	print("erro ao criar tabelas")

@app.route("/")
def inicio():
	global logado
	return render_template("inicio.html", logado = logado)
	

@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("listar_pessoas.html", users = p.Pessoa.select(), logado = logado)

@app.route("/ver_video")
def ver_video():
	return render_template("ver_video.html")

@app.route("/form_adicionar")
def form_adicionar():
	return render_template("form_adicionar.html")

@app.route("/adicionar_pessoa")#, endpoint = "listar_pessoas")
def adicionar_pessoa():
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	p.Pessoa.create(nom_pessoa = nome, endereco = endereco)
	return redirect("/listar_pessoas")

@app.route("/deletar_pessoa")
def deletar_pessoa():
	nome = request.args.get("nome")
	#gest.remover_da_tabela_nome(nome)
	return redirect("/listar_pessoas")

@app.route("/form_alterar")
def form_alterar():
	id = pegar("id")
	nome = pegar("nome")
	ende = pegar("endereco")
	pe=Pessoa(id, nome, ende)
	return render_template("form_alterar.html", p=pe)

@app.route("/alterar_pessoa")
def alterar_pessoa():
	id = pegar("id")
	nome = pegar("nome")
	ende = pegar("endereco")
	#gest.alterar_por_id(id,nome,ende)
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
	print("--------------", logado)
	if logado:
		pass
	else:
		user = request.form["user"]
		print("--------------", user)
		#senha_comparar = gest.buscar_senha(user)
		senha_comparar = p.Contas.select().where(p.Contas.user == user)
		print(senha_comparar[0].passwd)
		print("--------------", senha_comparar)
		if senha_comparar:
			m.update(request.form["passwd"].encode())
			senha = m.hexdigest()
			print("--------------", senha)
			if senha == senha_comparar[0].passwd:
				logado = True
				m = md5()
				#session["user"] = user
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
	#gest.cadastrar_user(user, senha)
	return redirect("/")

		
@app.route("/logout")
def logout():
	global logado
	logado = False
	return redirect("/")


app.run(debug=True)