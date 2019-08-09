"49. Requisições de exame de sangue podem conter as seguintes informações:\
• a data na qual foi feita a requisição;\
• o nome do paciente;\
• o nome do médico;\
• os exames específicos solicitados (por exemplo: triglicerídeos, colesterol, etc).\
Cada exame possui um nome, um preço e um prazo (em dias) para ter o resultado liberado.\
Um laboratório de análises clínicas deseja controlar as requisições que recebe para realizar.\
Faça as seguintes tarefas:\
(a) Elabore um registro (anotações, tabelas, diagramas, etc) que permita controlar as\
requisições do laboratório.\
(b) Crie classes (com uso do peewee) que permitam armazenar as informações das requisições.\
(c) Faça o teste das classes."

from peewee import *
from os import system

#get_through_model

db = SqliteDatabase("49.db")

class Modelo(Model):
	class Meta():
		database = db

class Pessoa(Modelo):
	nome = CharField()

class Medico(Pessoa):
	pass

class Paciente(Pessoa):
	medico = ManyToManyField(Medico)

'''
class Exame(Modelo):
	paciente = ForeignKeyField(Paciente)
	medico = ForeignKeyField(Medico)
	data_requisicao = DateField()#9999-99-99
	tipo_exame = CharField() '''

if __name__ == '__main__':
	system("rm -f 49.db")
	db.connect()
	db.create_tables([Paciente.medico.get_through_model(), Medico])
	m = Medico(nome = "Beltrano").save()
	Paciente(nome = "Fulano", medico = m ).save()
	
	#Exame(paciente = 1, medico = 1,data_requisicao = "9999-99-99",tipo_exame = "raio x").save()
	#q1 = Exame_Requisitado.select().where(Exame_Requisitado.paciente == Paciente.get_by_id(1))
	#print(q1[0].paciente.nome)

