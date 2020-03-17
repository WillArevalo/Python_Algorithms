# _*_ coding: utf-8 _*_
"""This module is for make a binary search. https://wiki.python.org/moin/TimeComplexity"""
import random
import time

def bubble_sort(lista):
    n = len(lista)
    iter = 0
    for i in range(n):
        for j in range(0, n - i -1): #O(n) * O(n) = O(n * n) = O(n**2)
            iter += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return(lista, iter)
    

if __name__ == "__main__":
    len_of_list = int(input("What length of list want? "))
    lista = [random.randint(0,10000) for i in range(len_of_list)]
    print(*lista, sep=' ')
    tic = time.time()
    sort_list, iter = bubble_sort(lista)
    toc = time.time()
    print(*sort_list, sep=',')
    print(f'Time of process {round(toc -tic, 4)} & iterations {iter}')