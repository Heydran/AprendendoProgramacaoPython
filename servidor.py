class Pessoa(object):
	def __init__(self, id, nome, endereco):
		self.id = id
		self.nome = nome
		self.endereco = endereco




#lista = [Pessoa("Lester","(560) 483-0293","São Paulo"),Pessoa("Solomon","(852) 535-1460","Quebec"),Pessoa("Kane","(342) 663-1815","Västra Götalands län"),Pessoa("Jeanette","(491) 924-6893","Provence-Alpes-Côte d'Azur"),Pessoa("Herman","(234) 414-9654","Île-de-France"),Pessoa("Joseph","(274) 796-9678","Oyo"),Pessoa("Blythe","(633) 709-8290","Västra Götalands län"),Pessoa("Bradley","(258) 860-2514","West-Vlaanderen"),Pessoa("Ashton","(355) 140-9940","LOM"),Pessoa("Russell","(999) 750-6924","Zuid Holland")]



from flask import Flask, render_template, request, redirect, session
from sql_site import GerenciadorSite as gest
from hashlib import md5
gest = gest()
gest.criar_tabela()

app = Flask("__name__")
app.config["secret_key"] = 'senha'
m = md5()
logado = False
pegar = lambda x: request.args.get(x)
pegar2 = lambda x: request.form[x]
@app.route("/")
def inicio():
	global logado
	return render_template("inicio.html", logado = logado)
	

@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("listar_pessoas.html", users = gest.listar_tabela(), logado = logado)

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
	gest.adicionar_na_tabela(nome,endereco)		
	#url_for("listar_pessoas")
	#return render_template("listar_pessoas.html", users = gest.listar_tabela())
	return redirect("/listar_pessoas")

@app.route("/deletar_pessoa")
def deletar_pessoa():
	nome = request.args.get("nome")
	gest.remover_da_tabela_nome(nome)
	return redirect("/listar_pessoas")

@app.route("/form_alterar")
def form_alterar():
	id = pegar("id")
	nome = pegar("nome")
	ende = pegar("endereco")
	p=Pessoa(id, nome, ende)
	return render_template("form_alterar.html", p=p)

@app.route("/alterar_pessoa")
def alterar_pessoa():
	id = pegar("id")
	nome = pegar("nome")
	ende = pegar("endereco")
	gest.alterar_por_id(id,nome,ende)
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
		senha_comparar = gest.buscar_senha(user)
		print("--------------", senha_comparar)
		if senha_comparar:
			m.update(request.form["passwd"].encode())
			senha = m.hexdigest()
			print("--------------", senha)
			if senha == senha_comparar:
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
	m.update(senha)
	senha = m.hexdigest()
	gest.cadastrar_user(user, senha)
	return redirect("/")

		
@app.route("/logout")
def logout():
	global logado
	logado = False
	return redirect("/")


app.run(debug=True)