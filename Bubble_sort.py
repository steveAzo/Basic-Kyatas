def bubble_sort(list_of_number):
    size = len(list_of_number)
    for i in range(size):
        for j in range(0, size - i - 1):
            if list_of_number[j] > list_of_number[j + 1]:
                list_of_number[j] , list_of_number[j + 1] = list_of_number[j + 1] , list_of_number[j]
    return list_of_number
    
