"47. Um jardim possui várias plantas. Um jardineiro deseja controlar as plantas que mantém nos \
diversos jardins em que atua. Uma planta possui nome, nome científico e tamanho da folha \
(pequena, média ou grande). Sobre esse contexto, faça as seguintes tarefas: \
(a) Elabore um registro, da melhor forma possível (linhas, tabela, diagrama, etc), que \
permita ao jardineiro possa anotar as plantas que cuida em cada jardim. \
(b) Elabore classes, com uso do peewee, que possam armazenar as informações do sistema, \
em substituição às anotações realizadas no item anterior. \
(c) Faça o teste das classes"

from peewee import *

db = SqliteDatabase("Planta.db")

class Modelo(Model):
	class Meta:
		database = db


class Jardim(Modelo):
	nome = CharField()


class Planta(Modelo):
	nome = CharField()
	nome_cientifico = CharField()
	tamanho_da_folha = CharField()
	jardim = ForeignKeyField(Jardim)

class Planta_do_Jardim(Modelo):
	jardim_id = 

if __name__ == '__main__':
	db.connect()
	db.create_tables([Jardim, Planta])
	#p1 = Planta(nome = "orquidea", nome_cientifico = "orquedeos", tamanho_da_folha = "infinito", jardim = 1).save()
	q1 = Planta.select()
	for i in q1:
		print(i.nome, i.nome_cientifico, i.tamanho_da_folha)
	#j1 = Jardim(nome = "label_name_jardin").save()
	q2 = Jardim.select().where(Jardim.jardim_id == Planta.jardim)
	
