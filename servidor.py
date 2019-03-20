class Pessoa(object):
	def __init__(self, nome,  telefone, endereco):
		self.nome = nome
		self.telefone = telefone
		self.endereco = endereco
lista = [Pessoa("Lester","(560) 483-0293","São Paulo"),Pessoa("Solomon","(852) 535-1460","Quebec"),Pessoa("Kane","(342) 663-1815","Västra Götalands län"),Pessoa("Jeanette","(491) 924-6893","Provence-Alpes-Côte d'Azur"),Pessoa("Herman","(234) 414-9654","Île-de-France"),Pessoa("Joseph","(274) 796-9678","Oyo"),Pessoa("Blythe","(633) 709-8290","Västra Götalands län"),Pessoa("Bradley","(258) 860-2514","West-Vlaanderen"),Pessoa("Ashton","(355) 140-9940","LOM"),Pessoa("Russell","(999) 750-6924","Zuid Holland")]



from flask import Flask, render_template
app = Flask("__name__")
@app.route("/")
def inicio():
	return render_template("inicio.html")
@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("listar_pessoas.html", users = lista)

@app.route("/ver_video")
def ver_video():
	return render_template("ver_video.html")

app.run()