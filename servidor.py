class Pessoa(object):
	def __init__(self, nome, idade, sexo):
		self.nome = nome
		self.idade = idade
		self.sexo = sexo
lista = [Pessoa("André","0","INDEFINIDO"),Pessoa("Heydran","Infinita","TODOS")]



from flask import Flask, render_template
app = Flask("__name__")
@app.route("/")
def inicio():
	return render_template("inicio.html")
@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("listar_pessoas.html", users = lista)
app.run()