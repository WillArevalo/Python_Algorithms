# _*_ coding: utf-8 _*_
"""Algorithm for sort lists"""

import random, time

def insertion_sort(lista):
    i = 0
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            i += 1
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        i += 1
        lista[posicion_actual] = valor_actual
    return(lista, i)

if __name__ == "__main__":
    len_of_list = int(input("How big should the list be? "))
    lista = [random.randint(0,10000) for i in range(len_of_list)]
    print(*lista, sep=" ")
    tic = time.time()
    sort_list, i = insertion_sort(lista)
    toc = time.time()
    print(*sort_list, sep=" ")
    print(f'The list is sort in {round(toc-tic,4)}secs in {i} iterations')
    print(*sort_list, sep=",")