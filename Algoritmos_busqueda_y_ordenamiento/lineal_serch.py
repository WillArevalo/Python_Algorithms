# _*_ coding: utf-8 _*_
"""
This module is for make a lineal search.
 https://wiki.python.org/moin/TimeComplexity
"""
import random

def lineal_search(lista, objetivo):
    """Lineal Search."""
    i = 0
    match = False
    for el in lista:
        i += 1
        print(f'Iteracion {i}')
        if el == objetivo:
            match = True
            break
    
    return match

if __name__ == "__main__":
    len_of_list = int(input("What length of list want? "))
    objetivo = int(input('What is the number for search? '))
    lista = [random.randint(0,100) for i in range(len_of_list)]
    print(*lista, sep=", ")
    encontrado = lineal_search(lista, objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista.')
