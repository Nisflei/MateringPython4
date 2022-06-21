produtos = [
    {'Produto': 'MILHO',  'Frete': 0.90, 'Peso_kg': 5500.0, 'Origem': 'MT', 'Destino': 'SP'},
    {'Produto': 'SOJA',   'Frete': 0.55, 'Peso_kg': 4300.0, 'Origem': 'MS', 'Destino': 'SP'},
    {'Produto': 'ALGODÃO','Frete': 0.13, 'Peso_kg': 3000.0, 'Origem': 'GO', 'Destino': 'MT'},
    {'Produto': 'MILHO',  'Frete': 0.49, 'Peso_kg': 8000.0, 'Origem': 'MS', 'Destino': 'MT'},
    {'Produto': 'MILHO',  'Frete': 0.22, 'Peso_kg': 5000.0, 'Origem': 'MS', 'Destino': 'MT'},
    {'Produto': 'ADUBO',  'Frete': 0.79, 'Peso_kg': 4500.0, 'Origem': 'SP', 'Destino': 'MS'},
    {'Produto': 'SOJA',   'Frete': 0.31, 'Peso_kg': 8000.0, 'Origem': 'GO', 'Destino': 'SP'},
    {'Produto': 'RAÇÃO',  'Frete': 0.27, 'Peso_kg': 1500.0, 'Origem': 'SP', 'Destino': 'MS'},
    {'Produto': 'ARROZ',  'Frete': 1.90, 'Peso_kg': 5300.0, 'Origem': 'RS', 'Destino': 'PR'},
]

print(produtos)

#1 Colocar em order de peso_kg

produtos.sort(key= lambda elemento: elemento['Peso_kg'])
print(f"Produto ordenado por Peso: {produtos}");

#1 Organizar por Origem + Produto

produtos.sort(key= lambda elemento: elemento['Origem'] and elemento['Produto'])
print(f"Produto ordenado por Origem+Produto: {produtos}");


#2 Vamos extrair somente os preços da lista

precos = list(map( lambda elemento: elemento['Frete'], produtos))
print(precos)

#3 Devido ao combustivel, calcular 10% na tabela de "precos"

precos = list(map(lambda elemento: round(elemento * 1.10, 2), precos))
print(precos)

#Reajustar a tabela de produtos em 10% para o "FRETE" somente Origem=SP"

def calc_valor(origem,valor):
    if origem == 'SP':
        return round(valor * 1.10,2)
    return valor

produtos = list(map(lambda elemento: {**elemento, 'Frete': calc_valor(elemento['Origem'],elemento['Frete'])}, produtos))
print(f"Frete Reajustado: {produtos}")

#4 Temos que transportar MILHO, sendo assim gerar uma nova LISTA

produto_Milho = list(filter(lambda elemento: str.upper(elemento['Produto']) == 'MILHO', produtos))
print(f"produtoMilho: {produto_Milho}")

# milho e soja para filtrar
#                                               {     condição 1                         } ou {   condição 2                          }
produto_MilhoSoja = list(filter(lambda elemento: str.upper(elemento['Produto']) == 'MILHO' or str.upper(elemento['Produto']) == 'SOJA', produtos))
print(f"produtoMilho: {produto_MilhoSoja}")

#5 Apresente o valor total ( milho e soja) considerando frete * peso

from functools import reduce

Total_milhoSoja = reduce(lambda acumulador,elemento: acumulador + (elemento['Frete'] * elemento['Peso_kg']), produto_MilhoSoja,0)
print(f"Total de MilhoSoja: {Total_milhoSoja}")


produto_MilhoSojaTotal =  list(map(lambda elemento:{**elemento, 'Total': elemento['Frete'] * elemento['Peso_kg'] },produto_MilhoSoja))
print(produto_MilhoSojaTotal)
