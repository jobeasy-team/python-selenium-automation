"""
Even First
Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
 You are required to solve it without allocating additional storage (operate with the input array).
Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
"""

# def even_first(arr):
#     next_even = 0
#     next_odd = len(arr) - 1
#
#     while next_even < next_odd:
#         if arr[next_even] % 2 == 0:
#             next_even += 1
#         else:
#             arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
#             next_odd -= 1
#
# test_array = [7, 3, 5, 6, 4, 10, 3, 2]
# print(test_array)
# even_first(test_array)
# print(test_array)



"""
Increment a Number
Write a program that takes as input an array of digits encoding a nonnegative decimal integer 
D and updates the array to represent the integer D + 1.
For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0]
"""

def increment_number(list):
    list[-1] += 1
    for i in reversed(range(1, len(list))):
        if list[i] != 10:
            break
        list[i] = 0
        list[i - 1] += 1
    if list[0] == 10:
        list[0] = 1
        list.append(0)

    return list

test_array = [9, 9, 9]
print(test_array)
print(increment_number(test_array))
