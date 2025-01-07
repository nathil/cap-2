#1- Dada uma lista de string, faça uma função para obter uma lista somente com os elementos cujo tamanho da 
#string seja menor que 10. A lista resultante deve estar ordenada em ordem alfabética. Retorne a lista resultante.

#1o modo

def listaRetorno(lista): 
    menorLista = []
    for item in lista:
        if len(item) < 10: 
            menorLista.append(item)
    return sorted(menorLista) 

#2o modo

def listaRetorno2(lista):
    for item in lista.copy():
        if len(item) >= 10:
            lista.remove(item)
    return sorted(lista)

#3o modo

def listaRetorno3(lista):
    menorLista = [item for item in lista if len(item) < 10]
    return sorted(menorLista)
