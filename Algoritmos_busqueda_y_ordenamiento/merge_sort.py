# _*_ coding: utf-8 _*_

"""Algorithm for sort list"""

import random, time

def merge_sort(lista, i=0):
    if len(lista) > 1:
        mid = len(lista) // 2

        #divide the list until the length of the list if is big than 1
        left = lista[:mid]
        right = lista[mid:]
        print(left, '*' * 5, right)

        #call the middle with recursive function
        merge_sort(left, i)
        merge_sort(right, i)

        # iterators for sublists
        j, k = 0 , 0
        # iterator for main list
        l = 0

        while j < len(left) and k < len(right):
            if left[j] < right[k]:
                lista[l] = left[j]
                j += 1
            else:
                lista[l] = right[k]
                k += 1

            l += 1
            i += 1

        while j < len(left):
            lista[l] = left[j]
            j += 1
            l += 1
            i += 1

        while k < len(right):
            lista[l] = right[k]
            k += 1
            l += 1
            i += 1

        print(f'left {left} & right {right}')
        print('Lista -> ',lista)
        print('-' * 10, ' Finish Iteration ', i, " ", '-' * 10)

    return(lista, i)

if __name__ == "__main__":
    len_of_list = int(input("How big should the list be? "))
    lista = [random.randint(1,10000) for i in range(len_of_list)]
    print(*lista, sep=" ")
    tic = time.time()
    sort_list, i = merge_sort(lista)
    toc = time.time()
    print(f'the list is sort in {round(toc-tic, 4)}secs in {i} iterations')
    print(*lista, sep=",")
