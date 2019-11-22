#Animes
from peewee import *

db = Mysqldatabase("Animes.db")

class Modelo(Model):
	class Meta:
		database = db

class Episodio(Modelo):
	nome = CharField()
	duracao = CharField()
	numero = CharField()
	arquivo = CharField()

class Genero(Modelo):
	nome = CharField()
	descricao = CharField()

class Personagem(Mdelo):
	nome = CharField()
	idade = CharField()
	

class Anime(Modelo):
	nome = CharField()
	generos = ForeignkeyField(Genero)
	data = CharField()
	episodios = ForeignkeyField(Episodio)
	personagens = ForeignkeyField(Personagem)

class Album(Modelo):
	nome = CharField()
	criador = CharField()
	animes = ForeignkeyField(Anime)


