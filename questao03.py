#3- Dada uma lista de string e uma lista de números inteiros, faça uma função para obter uma lista de string onde o 
#tamanho do elemento é menor ou igual ao valor do número inteiro de índice correspondente. Retorne a lista resultante.

#1o modo

def funcao(lista, lista2): 
    novaLista = []
    for i, item in enumerate(lista):
        if len(item) <= lista2[i]:
            novaLista.append(item)
    return novaLista

#2o modo

def funcao2(lista, lista2):
    novaLista = []
    for itemLista, itemLista2 in zip(lista, lista2):
        if len(itemLista) <= itemLista2:
            novaLista.append(itemLista)
    return novaLista

#3o modo

def funcao3(lista, lista2):
    for i, item in enumerate(lista.copy()):
        if len(item) > lista2[i]:
            lista.remove(item)
    return lista

    
    

    
