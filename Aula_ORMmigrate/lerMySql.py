from databaseMySql import dbMy, PetAdocao

print(">--- Lista de Dados no MySQL")

pets_dbMy = dbMy.session.query(PetAdocao).all()
for pet in pets_dbMy:
    print(f'id: {pet.id} - Apelido:{pet.apelido}')

dbMy.session.close()