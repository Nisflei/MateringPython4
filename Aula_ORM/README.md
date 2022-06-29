Python - ORM com Python - SQLAlchemy  

# Preparando as dependencias

python -m pip install --upgrade pip

pip install
- flask: microframework para criação de aplicativos web
- sqlalchemy: ORM para trabalhar com banco de dados
- flask-sqlalchemy: integração entre flask e sqlalchemy
- pymysql: driver de conexão com o banco de dados MySQL
- cryptography

# Lembre-se de configura a String de Conexão 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<userId>:<Senha>@localhost:3306/<BancoDados>'

# Voce precisar criar as Classes no projeto

- Essas Classes serão o ORM (Object Relational Modelling) 
- Não esquece de definir as informações de conexão

# Agora podemos carregar o projeto para criar as tabelas:
 - Python Console: 
 --from Model import db
 --db.create_all()
 ou 
 --db.drop_all()
 
# Lembre-se de sempre usar as operações

  -db.session.add(<objeto>)
  -db.session.delete(<objeto>)
  -db.session.commit()
  -db.session.query(<Classe>).all()