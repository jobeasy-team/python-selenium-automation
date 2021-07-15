# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s
# arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def below_the_mean(list):
    result = 0
    for num in list:
        result += num
    print(f'Total = ' + str(result))
    mean = result / len(list)
    print(f'Arithmetical mean = ' + str(mean))

    for element in list:
        new_list = []
        if element < mean:
            new_list.append(element)
            print(new_list)








below_the_mean([1, 3, 5, 6, 4, 10, 2, 3])





# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def two_lowest_elements(list2):
    low1 = list2[0]
    low2 = list2[1]
    for ele in list2:
        if ele < low1:
            low1 = ele
        elif ele < low2:
            low2 = ele
    print(f'The two lowest elements are ' + str(low1) + ' and ' + str(low2))

two_lowest_elements([198, 3, 1, 9, 10, 9, 2])




