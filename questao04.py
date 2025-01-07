#4 - Dada uma lista onde cada elemento corresponde a uma lista de números inteiros, faça umafunção para construir 
#uma lista de listas onde a soma dos elementos da lista de uma determinada posição é maior que a soma dos elementos da 
#lista da próxima posição. Retorne a lista resultante. 

#1o modo

def funcao(lista): 
    novaLista = []
    for item, itemProx in zip(lista, lista[1:]):
        if sum(item) > sum(itemProx):
            novaLista.append(item)
    return novaLista

#2o modo

