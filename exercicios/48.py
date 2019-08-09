"48. Plantas diferentes necessitam de manutenção em períodos diferentes. Por exemplo, uma\
espécie deve ser podada a cada dois meses, enquanto outra espécie precisa ser aparada a cada\
120 dias. Insira no controle de plantas da questão anterior a esta as seguintes informações:\
• o período (em dias) de poda de cada planta;\
• a data em que a planta foi plantada no jardim.\
Repita os itens b) e c) da questão anterior, com as novas informações inseridas nesta questão."


from peewee import *
from os import system

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
	periodo_poda = IntegerField()

class Planta_do_Jardim(Modelo):
	jardim = ForeignKeyField(Jardim)
	planta = ForeignKeyField(Planta)
	data_plantada = CharField()

if __name__ == '__main__':
	system("rm -f Planta.db")
	db.connect()
	db.create_tables([Jardim, Planta, Planta_do_Jardim])
	Planta(nome = "orquidea", nome_cientifico = "orquedeos", tamanho_da_folha = "infinito", jardim = 1, periodo_poda = 30).save()
	q1 = Planta.select()
	for i in q1:
		print(i.nome, i.nome_cientifico, i.tamanho_da_folha)
	Jardim(nome = "label_name_jardin").save()

	Planta_do_Jardim(jardim = 1, planta = 1,data_plantada = "12/05/2003").save()
	
	q2 = Planta_do_Jardim.select().where(Planta_do_Jardim.planta == Planta.get_by_id(1))
	
	print(q2[0].data_plantada)