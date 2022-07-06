from databaseSQLite import dbLite,PetAdocao, Tutor
from datetime import datetime

## -- Recriar Banco de dados

dbLite.drop_all()
dbLite.create_all()

pets = [
    PetAdocao('Furação','docil',datetime.strptime('2021-09-26', '%Y-%m-%d'),True,'Ana Maria Braga','ana@gmail.com'),
    PetAdocao('Fofinho', 'bravo', datetime.strptime('2022-01-26', '%Y-%m-%d'), True, 'Fausto Silva', 'fausto@gmail.com'),
    PetAdocao('Maiau', 'docil', datetime.strptime('2022-05-26', '%Y-%m-%d'), False, 'Pedro Bial','pedro@gmail.com'),
    PetAdocao('Costelinha', 'bravo', datetime.strptime('2021-12-26', '%Y-%m-%d'), False, 'Ratinho', 'ratinho@gmail.com')
]
print(pets)
print('>---- Lista de elementos para carregar no SQLite')

for linha in pets:
    print(f'Dados: id- {linha.id } - {linha.apelido} - {linha.responsavel} - {linha.dataregistro}')
    dbLite.session.add(linha)
    dbLite.session.commit()
    print(f'Dados: id- {linha.id } - {linha.apelido} - {linha.responsavel} - {linha.dataregistro}')

print(pets)

# Carregar Tutor

tutor_1 = Tutor('Ana Maria Braga','Rua que sobe','1199898989',pets[3].id)
tutor_2 = Tutor('Fausto Silva','Rua X','1199898989',pets[0].id)

dbLite.session.add(tutor_1)
dbLite.session.add(tutor_2)
dbLite.session.commit()
print(tutor_1)
print(tutor_2)

dbLite.session.close()

