import os

from sqlalchemy import create_engine,Column,String
from sqlalchemy.orm import sessionmaker, declarative_base

os.system("cls||clear")

APLICATIVO=create_engine("sqlite:///meubanco.db")

Session=sessionmaker(bind=APLICATIVO)
session=Session()

Base=declarative_base()

class Aluno(Base):
    __tablename__="alunos"

    ra=Column("ra",String, primary_key=True)
    nome=Column("nome",String)
    sobrenome=Column("sobrenome",String)
    email=Column("email",String)
    senha=Column("senha",String)

    def __init__(self,ra:str,nome:str,sobrenome:str,email:str,senha:str):
        self.ra=ra
        self.nome=nome
        self.sobrenome=sobrenome
        self.email=email
        self.senha=senha

Base.metadata.create_all(bind=APLICATIVO)

print("Solicitando dados do usuário")
inserir_ra=input("Digite o seu RA: ")
inserir_nome=input("Digite o seu nome: ")
inserir_sobrenome=input("Digite o seu sobrenome: ")
inserir_email=input("Digite o seu email: ")
inserir_senha=input("Digite a sua senha: ")

aluno=Aluno(ra=inserir_ra,nome=inserir_nome,sobrenome=inserir_sobrenome,email=inserir_email,senha=inserir_senha)
session.add(aluno)
session.commit

lista_alunos=session.query(Aluno).all()

os.system("cls||clear")

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} {aluno.sobrenome} - {aluno.email} - {aluno.senha}")