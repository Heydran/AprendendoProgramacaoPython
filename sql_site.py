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

class GerenciadorPessoa(object):
	def __init__(self):	
		self.engine = create_engine("mysql+mysqlconnector://root:root@localhost")
		self.conn = self.engine.connect()
		self.conn.execute("create schema if not exists PessoaAndre")
		self.conn.execute("use PessoaAndre")
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
		resultado = self.s.query(Pessoa).filter(Pessoa.id == id).update({"endereco":(endereco)})
		resultado = self.s.query(Pessoa).filter(Pessoa.id == id).update({"nome":(nome)})
		self.s.commit()

	def listar_tabela(self):
		resultados = self.s.query(Pessoa)
		pessoas = []
		for resultado in resultados:
			pessoas.append(Pessoa(id = resultado.id, nome = resultado.nome, endereco = resultado.endereco))
		return pessoas

if __name__ == '__main__':
	o=GerenciadorPessoa()
	o.alterar_por_id(2,"oi", "io")