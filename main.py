import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


os.system("cls||clear")
# Criando o banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

# CRUD



print("Solicitando dados para o usuário.")
inserir_nome = input("Digite o seu nome: ")
inserir_email = input("Digite o seu email: ")
inserir_senha = input("Digite a sua senha: ")

cliente = Cliente(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(cliente)
session.commit()



os.system("cls||clear")
print("\nAtualizando dados do usuário")
nome_cliente=input("Digite o nome do cliente que será atualizado: ")
email_cliente=input("Digite o email do cliente que será atualizado: ")
senha_cliente=input("Digite a senha do cliente que será atualizado: ")

cliente=session.query(Cliente).filter_by(email=email_cliente).first()
cliente=session.query(Cliente).filter_by(nome=nome_cliente).first()
cliente=session.query(Cliente).filter_by(senha=senha_cliente).first()

if cliente:
    cliente.nome=input("Digite o seu nome: ")
    cliente.email=input("Digite o seu email: ")
    cliente.senha=input("Digite a sua senha:")

    session.commit()

else:
    print("Cliente não encontrado")


nome_cliente=input("Digite o nome do cliente que será excluido: ")
email_cliente=input("Digite o email do cliente que será excluido: ")
senha_cliente=input("Digite a senha do cliente que será excluido: ")


cliente=session.query(Cliente).filter_by(email=email_cliente).first()
cliente=session.query(Cliente).filter_by(nome=nome_cliente).first()
cliente=session.query(Cliente).filter_by(senha=senha_cliente).first()

print("Consultando os dados apenas de um cliente.")

nome_cliente=input("Digite o nome do cliente: ")

cliente=session.query(Cliente).filter_by(nome=nome_cliente).first()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente {cliente.nome} excluido com sucesso")

else:
    print("Cliente não encontrado")


print("\nExibindo os dados de todos os usuários na tabela.")
lista_clientes = session.query(Cliente).all()

os.system("cls||clear")
for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

#Fechando conexão

session.close()
