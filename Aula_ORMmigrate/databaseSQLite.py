import sqlite3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancoLite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_ECHO'] = True

dbLite = SQLAlchemy(app)

#Definir Class que deve ser representada no banco de dados
class PetAdocao(dbLite.Model):
    id = dbLite.Column(dbLite.Integer, primary_key=True)
    apelido = dbLite.Column(dbLite.String(60))
    perfil = dbLite.Column(dbLite.String(100))
    dataregistro =dbLite.Column(dbLite.DateTime())
    castrado = dbLite.Column(dbLite.Boolean, default=True)
    responsavel = dbLite.Column(dbLite.String(100))
    contato = dbLite.Column(dbLite.String(100))

    def __init__(self, apelido, perfil,dataregistro,castrado,responsavel,contato):
        self.apelido = apelido
        self.perfil = perfil
        self.dataregistro = dataregistro
        self.castrado = castrado
        self.responsavel = responsavel
        self.contato = contato
