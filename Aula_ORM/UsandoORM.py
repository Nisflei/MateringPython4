from Model import PetAdocao,db
from datetime import datetime

#Dados obtido através de uma entrada(exemplo: formulario)

fofinho = PetAdocao('Fofinho', 'bravo', datetime.strptime('28/07/2022', '%d/%m/%Y'), True, 'Fausto Silva','fausto@teste.com.br')

print(f"{fofinho.apelido} - {fofinho.id}")
print(fofinho.responsavel)

# Salva no Banco de dados
db.session.add(fofinho)
db.session.commit()

# --------------------

pets = [
    PetAdocao('Furação','docil',datetime.strptime('2021-09-26', '%Y-%m-%d'),True,'Ana Maria Braga','ana@gmail.com'),
    PetAdocao('Fofinho', 'bravo', datetime.strptime('2022-01-26', '%Y-%m-%d'), True, 'Fausto Silva', 'fausto@gmail.com'),
    PetAdocao('Maiau', 'docil', datetime.strptime('2022-05-26', '%Y-%m-%d'), False, 'Pedro Bial','pedro@gmail.com'),
    PetAdocao('Costelinha', 'bravo', datetime.strptime('2021-12-26', '%Y-%m-%d'), False, 'Ratinho', 'ratinho@gmail.com')
]
print(pets)

print('>---- Lista de elementos para carregar no BD')

for linha in pets:
    print(f'Dados: id- {linha.id } - {linha.apelido} - {linha.responsavel} - {linha.dataregistro}')
    db.session.add(linha)
    db.session.commit()
    print(f'Dados: id- {linha.id } - {linha.apelido} - {linha.responsavel} - {linha.dataregistro}')
    print("-------")
print(pets)

# Consulta no Banco de Dados

print(">---- Lendo os dados no Banco")
pets_bd = db.session.query(PetAdocao).all()

for pet in pets_bd:
    print(f'id: {pet.id} - {pet.apelido} - {pet.perfil}')

# Consultar apenas 1 registro

pets_temp = PetAdocao.query.filter_by(id=5).first()
print(f"id: {pets_temp.id} - {pets_temp.apelido}")

# Remover 1 registro

print(f">---- Removendo: {pets_temp.id} - {pets_temp.apelido}")
db.session.delete(pets_temp)
db.session.commit()


print("Terminou..!!")
