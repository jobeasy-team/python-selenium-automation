#Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def lowest_elements(arr):
    arr.sort()
    return arr[:2]


test_list = [198, 3, 4, 9, 10, 9, 2]
print(lowest_elements(test_list))