from databaseSQLite import dbLite,PetAdocao

print(">--- Lista de Dados no SQLite")

pets_dblite = dbLite.session.query(PetAdocao).all()
for pet in pets_dblite:
    print(f'id: {pet.id} - Apelido:{pet.apelido}')



dbLite.session.close()