from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# habilitar conexão no Banco de Dados

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://userbd:Teste#1234@localhost:3306/BD_ORM'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
#---------


#Definir Class que deve ser representada no banco de dados
class PetAdocao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    apelido = db.Column(db.String(60))
    perfil = db.Column(db.String(100))
    dataregistro =db.Column(db.DateTime())
    castrado = db.Column(db.Boolean, default=True)
    responsavel = db.Column(db.String(100))
    contato = db.Column(db.String(100))

    def __init__(self, apelido, perfil,dataregistro,castrado,responsavel,contato):
        self.apelido = apelido
        self.perfil = perfil
        self.dataregistro = dataregistro
        self.castrado = castrado
        self.responsavel = responsavel
        self.contato = contato


## -- Recriar Banco de dados

db.drop_all()  # tem q remover quando finalizar os testes
db.create_all()