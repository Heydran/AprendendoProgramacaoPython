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
		self.engine = create_engine("mysql+mysqlconnector://root:root@localhost/PessoaAndre")
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

	def remover_da_tabela_id(self, num):
		self.s.query(Pessoa).filter(Pessoa.id == num).delete()
		self.s.commit()

	def buscar_na_tabela(self, nome):
		resultados = self.s.query(Pessoa).filter(Animes.nome == nome)
		pessoas = []
		for resultado in resultados:
			pessoas.append(Animes(id = resultado.id, nome = resultado.nome, genero = resultado.genero))
		return pessoas

	def listar_tabela(self):
		resultados = self.s.query(Pessoa)
		animes = []
		for resultado in resultados:
			pessoas.append(Animes(id = resultado.id, nome = resultado.nome, genero = resultado.genero))
		return pessoas