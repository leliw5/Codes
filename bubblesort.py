# Bubble sort

import random


def random_table(size, start, end):
    tab = []
    for i in range(size):
        tab.append(random.randint(start, end))
    return tab


def bubble_sort(table):
    for i in range(len(table)):
        j = len(table) - 1
        while j > i:
            if table[j] < table[j-1]:
                table[j], table[j-1] = table[j-1], table[j]
            j -= 1
    return table


a = random_table(10, 1, 10)
print(a)
bubble_sort(a)
print(a)