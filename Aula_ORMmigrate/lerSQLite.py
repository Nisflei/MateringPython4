from databaseSQLite import dbLite,PetAdocao, Tutor

print(">--- Lista de Dados no SQLite")

pets_dblite = dbLite.session.query(PetAdocao).all()
for pet in pets_dblite:
    print(f'id: {pet.id} - Apelido:{pet.apelido}')

print(">--- Lista de Tutores")
tuto_dblite = dbLite.session.query(Tutor).all()
for tt in tuto_dblite:
    print(f'id: {tt.id} - Nome: {tt.nome} - pet_id: {tt.petadocao_id}')

dbLite.session.close()