# _*_ coding: utf-8 _*_
"""
This module is for make a lineal search.
 https://wiki.python.org/moin/TimeComplexity
"""
import random

def binary_search(lista, comienzo, final, objetivo, i=0):
    i += 1
    print(f'Iteracion {i} se esta buscando el valor {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    if comienzo > final:
        return False
    medio = (comienzo + final) // 2
    if lista[medio] == objetivo:
        return True
    elif lista[medio] > objetivo:
        return binary_search(lista, comienzo, medio-1, objetivo, i)
    else:
        return binary_search(lista, medio+1, final, objetivo, i)

if __name__ == "__main__":
    len_of_list = int(input("What length of list want? "))
    objetivo = int(input('What is the number for search? '))
    lista = sorted([random.randint(0,100) for i in range(len_of_list)])
    encontrado = binary_search(lista, 0, len(lista), objetivo)
    print(*lista, sep=' ')
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista.')