
print(">--- MIGRACAO ------ <")

# --- Parte 1: Receber os dados do SQLite

from databaseSQLite import dbLite,PetAdocao

print(">--- Lista de Dados no SQLite")

pets_dblite = dbLite.session.query(PetAdocao).all()
for pet in pets_dblite:
    print(f'id: {pet.id} - Apelido:{pet.apelido}')
print(f'Obj SQLite: {pets_dblite}')

# --- Parte 2: Ativar conexão com o MySQL

from databaseMySql import dbMy, PetAdocao

# --- Compor a estrutura de dados no MySQL
dbMy.drop_all()
dbMy.create_all()

# -- Parte 3: Adicionar os pets_dblite (memoria) para o MySQL
print(f'Obj MySql')
for pet in pets_dblite:
    novoPet = PetAdocao(pet.apelido, pet.perfil, pet.dataregistro, pet.castrado, pet.responsavel, pet.contato)
    dbMy.session.add(novoPet)
    dbMy.session.commit()
    print(f'id: {novoPet.id} - Apelido:{novoPet.apelido}')

# --- Fechar conexões
dbLite.session.close()
dbMy.session.close()