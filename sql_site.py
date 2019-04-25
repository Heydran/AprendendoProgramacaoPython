try: 
	from sqlalchemy import Column, Integer, String, create_engine, update
except:
	from os import system
	system("pip3 install sqlalchemy")
	system("pip3 install mysql-connector")
	from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Pessoa(Base):
	__tablename__ = "Pessoa"	

	id = Column(Integer, primary_key = True, autoincrement=True)
	nome = Column(String(60), nullable = False)
	endereco = Column(String(120), nullable = False)

class Users(Base):
	__tablename__ = "Users"
	user = Column(String(20), primary_key = True)
	passwd = Column(String(128), nullable = False)
		

class GerenciadorSite(object):
	def __init__(self):	
		self.engine = create_engine("mysql+mysqlconnector://root:root@localhost")
		self.conn = self.engine.connect()
		self.conn.execute("create schema if not exists Site")
		self.conn.execute("use Site")
		self.conn.close()
		self.session = sessionmaker(bind = self.engine)
		self.s = self.session()

	def criar_tabela(self):
		Base.metadata.create_all(self.engine)

	def excluir_tabela(self):
		Base.metadata.drop_all(self.engine)

	def adicionar_na_tabela(self, nome, endereco, id = 0):
		pessoa = Pessoa(id = id, nome = nome, endereco = endereco)
		self.s.add(pessoa)
		self.s.commit()

	def remover_da_tabela_nome(self, nome):
		self.s.query(Pessoa).filter(Pessoa.nome == nome).delete()
		self.s.commit()

	def buscar_na_tabela(self, nome):
		resultados = self.s.query(Pessoa).filter(Pessoa.nome == nome)
		pessoas = []
		for resultado in resultados:
			pessoas.append(Pessoa(id = resultado.id, nome = resultado.nome, endereco = resultado.endereco))
		return pessoas

	def alterar_por_id(self, id, nome, endereco):
		self.s.query(Pessoa).filter(Pessoa.id == id).update({"endereco":(endereco)})
		self.s.query(Pessoa).filter(Pessoa.id == id).update({"nome":(nome)})
		self.s.commit()

	def listar_tabela(self):
		resultados = self.s.query(Pessoa)
		pessoas = []
		for resultado in resultados:
			pessoas.append(Pessoa(id = resultado.id, nome = resultado.nome, endereco = resultado.endereco))
		return pessoas

	def buscar_senha(self, user):
		resultados = self.s.query(Users).filter(Users.user == user)
		pessoas = []
		for resultado in resultados:
			pessoas.append(Users(user = resultado.user, passwd = resultado.passwd))
		return pessoas[0].passwd
		
	def cadastrar_user(self, user, passwd):
		user = Users(user = user, passwd = passwd)
		self.s.add(user)
		self.s.commit()

if __name__ == '__main__':
	o=GerenciadorSite()
	o.criar_tabela()
	a = o.buscar_senha("admin")
	print(a)
	#o.buscar_na_tabela('admin')