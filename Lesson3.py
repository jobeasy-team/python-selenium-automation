#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3


def my_sortedlist(example):
    example.sort()
    return example[:2]

test_data = [198, 3, 4, 9, 10, 9,2 ]
print(my_sortedlist(test_data))

#When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
#The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def mean_list(example):
    new_list = []
    l = sum(example) // len(example)
    for i in example:
        if i < l:
            new_list.append(i)
    return new_list
test_data = [1,3,5,6,4,10,2,3]

print(mean_list(test_data))