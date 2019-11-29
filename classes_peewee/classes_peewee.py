#char
#Animes
from peewee import *
from playhouse.shortcuts import model_to_dict

db = SqliteDatabase("Animes.db")

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

class Personagem(Modelo):
	nome = CharField()
	idade = CharField()
	
class Produto(Modelo):
	nome = CharField()
	data = CharField()
	generos = ManyToManyField(Genero)
	personagens = ManyToManyField(Personagem)
	episodios = ManyToManyField(Episodio)


class Anime(Modelo):
	nome = CharField()
	produto = ForeignKeyField(Produto)


class Diretor(Modelo):
	nome = CharField()
	cpf = CharField()
	salario = CharField()
	projetos = ManyToManyField(Anime)

class Estudio(Modelo):
	nome = CharField()
	diretor = ForeignKeyField(Diretor)
	animes = ManyToManyField(Anime)

class Filme(Modelo):
	produto = ForeignKeyField(Produto)
	estudio = ForeignKeyField(Estudio)

class Usuario(Modelo):
	nome = CharField()

class Album(Modelo):
	nome = CharField()
	criador = ForeignKeyField(Usuario)
	animes = ManyToManyField(Anime)
	filmes = ManyToManyField(Filme)




if __name__ == '__main__':
	
	db.connect()
	db.create_tables([Episodio, Genero, Personagem, Anime, Filme, Album, Produto, Diretor, Estudio, Usuario])
	db.create_tables([Produto.generos.get_through_model(), Produto.personagens.get_through_model(), Produto.episodios.get_through_model()])
	db.create_tables([Diretor.projetos.get_through_model()])
	db.create_tables([Estudio.animes.get_through_model()])
	db.create_tables([Album.animes.get_through_model(), Album.filmes.get_through_model()])

	ge = Genero(nome = "Ação", descricao = "Genero que tem muitas cenas que contem violencia").save()

	
	pe = Personagem(nome = "Escanor", idade = "25" ).save()
	ep = Episodio(nome = "O numero 1", duracao = "22:30",numero = "1",arquivo = "1.mp4").save()
	
	pr = Produto(nome = "Seven Signs", data = "00/00/0000").save()
	
	di = Diretor(nome = "Heydran", cpf = "000.000.000-00", salario = "9999999,99").save()
	es = Estudio(nome = "Heydran Productions", diretor = Diretor.get_by_id(1)).save()
	an = Anime(nome = "Seven Signs",produto = Produto.get_by_id(1), estudio = Estudio.get_by_id(1)).save()
	fi = Filme(produto = Produto.get_by_id(1), estudio = Estudio.get_by_id(1)).save()
	us = Usuario(nome = "Feuzer").save()
	al = Album(nome = "Os melhores de ação", criador = Usuario.get_by_id(1)).save()
	
	pr = Produto.get_by_id(1)
	pr.generos.add(Genero.get_by_id(1))
	pr.personagens.add([Personagem.get_by_id(1)])
	pr.episodios.add([Episodio.get_by_id(1)])

	di = Diretor.get_by_id(1)
	di.projetos.add([Diretor.get_by_id(1)])

	es = Estudio.get_by_id(1)
	es.animes.add([an])

	al = Album.get_by_id(1)
	al.animes.add([an])
	al.filmes.add([fi])

	
	for i in Album.select():
		print(i.nome)
		for j in i.animes:
			print(j.nome)
			print(j.produto.nome)
			for h in j.produto.episodios:
				print(h.nome)
				print(h.arquivo)

	print(list(map(model_to_dict, Album.select())))
