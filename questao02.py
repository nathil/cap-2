#2- Dada uma lista de número inteiros, e considerando a lista reversa, faça uma função para obter somente os 
#elementos que, para cada posição, são iguais na lista original e na reversa. Retorne a lista resultante.

#1o modo

def listasIguais(lista):
    elemIguais = []
    reversa = lista[::-1]
    for  i, item in enumerate(lista):
        if item == reversa[i]:
            elemIguais.append(item)
    return elemIguais

#2o modo

def listasIguais2(lista):
    elemIguais = []
    reversa = lista[::-1]
    for itemReversa, itemLista in zip(reversa, lista):
        if itemReversa == itemLista: 
            elemIguais.append(itemReversa)
    return elemIguais

#3o modo

listasIguais3 = lambda lista: [itemReversa for itemReversa, itemLista in zip(lista[::-1], lista) if itemReversa == itemLista]



    