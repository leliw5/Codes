def insertion_sort(alist):
    for index in range(len(alist)):

        current_value = alist[index]

        while index > 0 and alist[index-1] > current_value:
            alist[index] = alist[index-1]
            index = index-1

        alist[index] = current_value


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)