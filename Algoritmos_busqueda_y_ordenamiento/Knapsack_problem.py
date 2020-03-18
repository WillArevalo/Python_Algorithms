# _*_ coding: utf-8 _*_

"""Algorithm for combinatory optimization."""

import random

def comb_opti(knapsack, weights, values, len_of_list):
    """Optimize the combinatory."""
    if len_of_list == 0 or knapsack == 0: #Case of end recursive
        return 0

    if weights[len_of_list - 1] > knapsack:
        return comb_opti(knapsack, weights, values, len_of_list - 1)
        
    return max(values[len_of_list - 1] + comb_opti(knapsack - weights[len_of_list - 1], weights, values, len_of_list - 1),
                comb_opti(knapsack, weights, values, len_of_list - 1))

if __name__ == "__main__":
    len_of_list = int(input("how many elements must exist? "))
    values = [random.randint(0,100) for i in range(len_of_list)]
    weights = [random.randint(20,50) for i in range(len_of_list)]
    knapsack = random.randint(50, 150)
    print('-'*40, ' knapsack ', knapsack, ' ', '-'*40)
    print("Values\t",*values, sep="\t")
    print("Weights\t",*weights, sep="\t")

    result = comb_opti(knapsack, weights, values, len_of_list)
    print(f'The maximum values can get this knapsack is {result}')