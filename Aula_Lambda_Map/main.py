
print("Exemplo1 - LAMBDA")

def calculo_imposto(valor):
    return valor * 0.18

print("Valor do imposto para R$ 300:")
print(calculo_imposto(300));

print("Valor do imposto para R$ 100:")

calculo_imposto2 = lambda valor: valor * 0.18
print(calculo_imposto2(100));

# Impostos diferentes
def calculo_imp(imposto):
    return lambda x: x * imposto

icmsSP = calculo_imp(0.18)
icmsRJ = calculo_imp(0.12)

valorProduto = 500
print(f"Imposto para SP: {icmsSP(valorProduto)} - produto: R${valorProduto}")
print(f"Imposto para RJ: {icmsRJ(valorProduto)} - produto: R${valorProduto}")




print("Exemplo2 - MAP")

lista=[ ['Prod4', 400],
        ['Prod2', 200],
        ['Prod5', 500],
        ['Prod1', 100]
       ]

def funcOrder(linha):
    return linha[1];

#lista.sort(key=funcOrder)

lista.sort(key= lambda linha: linha[1])
print(lista);

#Calcular novos valores
listaValores = [100, 500, 200, 400]

novosValores =  list(map(lambda x: x*2, listaValores))
print(f"Novos Valores da Lista: {novosValores}")

#Usando Texto
animais = ["cao","gato","coelho","papagaio"]

novoAnimais = list(map( lambda elemento: str.upper(elemento), animais))
print(f"ListaAnimais: {novoAnimais}")

novaLista = list(map( lambda linha: str.upper(linha[0]), lista))
print(f"Nova ListaProdutos: {novaLista}")


print("Exemplo3 - FILTER")

lista=[ ['Prod4', 400],
        ['Prod2', 200],
        ['Prod5', 500],
        ['Prod1', 100]
       ]

listaFilter = list(filter( lambda item: item[1] >= 300, lista))
print(f"Filtro de valores >= 300: {listaFilter}")


print("Exemplo3 -  Filter")
lista=[2, 3, 4, 5, 6, 7, 8]

nova_lista_filter = list(filter(lambda x: (x/3 == 2), lista))
print(nova_lista_filter)

print("Exemplo4 - REDUCE")

from functools import reduce
lista=[2, 3, 4, 5, 6, 7, 8]
valorTotal = reduce( lambda acumulado, item: acumulado + item, lista)
print(f"Aplicando Reduce: {lista} - valor da Somatorio: {valorTotal}")


listaX=[ ['Prod4', 400],
        ['Prod2', 200],
        ['Prod5', 500],
        ['Prod1', 100]
       ]
##valorTotal = reduce( lambda acumulado, item: acumulado + item[1], listaX)
## voce precisa ISOLAR (criar novo lista) somente com a coluna de valor que deseja trabalhar




## !!!!Como apenas atualizar a LISTA e capturar os demais elementos que não foram alterados


listaX=[
    {'Prod': 'Prod4', 'Valor': 400},
    {'Prod': 'Prod1', 'Valor': 100},
    {'Prod': 'Prod2', 'Valor': 200},
    {'Prod': 'Prod5', 'Valor': 500}
]

valor_Dobro = list(map(lambda elemento: {**elemento, 'Valor': elemento['Valor'] * 2}, listaX))
print("Utilizanto uma lista como Objeto (atributo: valor)")
print(f"listaX:{listaX}")
print(f"listaD:{valor_Dobro}")

