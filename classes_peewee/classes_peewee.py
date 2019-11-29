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
	

class ModeloProduto(Modelo):
	nome = CharField()
	generos = ForeignkeyField(Genero)
	data = CharField()
	
	personagens = ForeignkeyField(Personagem)

class Filme(ModeloProduto):
	duracao = CharField()
	episodio = ForeignkeyField(Episodio)

class Anime(ModeloProduto):
	episodios = ManyToManyField(Episodio)


class Album(Modelo):
	nome = CharField()
	criador = CharField()
	animes = ForeignkeyField(Anime)


class Diretor(Modelo):
	nome = CharField()
	cpf = CharField()
	salario = CharField()
	projetos = ForeignkeyField(Anime)


class Estudio(Modelo):
	nome = CharField()
	diretor = ForeignkeyField()
	funcionarios = ManyToManyField(Funcionario)
	animes = ForeignkeyField()

class Usuario(Modelo):
	pass