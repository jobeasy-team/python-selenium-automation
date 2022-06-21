# Even Numbers First
# given an array,  rearrange elements without creating another array.

def even_first(arr):
    e, o = 0, len(arr) - 1
    while e < o:
        if arr[e] % 2 == 0:
            e += 1
        else:
            arr[e], arr[o] = arr[o], arr[e]
            o -= 1


list1 = [2, 3, 1, 4, 5, 6]

print(list1)
even_first(list1)
print(list1)

# Increment a Number
# Write a program that takes as input an array of digits encoding a nonnegative decimal
# integer D and updates the array to represent the integer D + 1.

# def inc_num(arr):
#     ind = len(arr) - 1
#     while ind >= 0 and arr[ind] == 9:
#         arr[ind] = 0
#         ind -= 1
#     if ind < 0:
#         arr.insert(0, 1)
#     else:
#         arr[ind] += 1


# list2 = [1, 2, 9]  # output [2, 3, 0]
# inc_num(list2)
# print(list2)
