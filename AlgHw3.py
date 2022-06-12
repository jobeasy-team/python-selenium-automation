# Below The Arithmetical Mean
# the program should return a list of all the elements below the original list’s arithmetical mean.

def below_arith_mean(l):
    mean = sum(l) // len(l)
    below_mean = []

    for value in l:
        if value < mean:
            below_mean.append(value)
    return below_mean


list1 = [1, 3, 5, 6, 4, 10, 2, 3]  # mean = 4.25
list2 = [1, 5, 8, 11, 55, 47, 42]  # mean = 24.14

print(below_arith_mean(list1))
print(below_arith_mean(list2))


# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.

def lowest_el(i):
    t_list1 = i.copy()
    two_smallest = []
    first_smallest = min(t_list1)
    two_smallest.append(first_smallest)
    t_list1.remove(first_smallest)
    sec_smallest = min(t_list1)
    two_smallest.append(sec_smallest)

    return two_smallest


list3 = [198, 3, 4, 9, 10, 9, 2]  # [2, 3]

print(lowest_el(list3))
