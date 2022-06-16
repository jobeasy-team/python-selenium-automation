# Even Numbers First
# given an array,  rearrange elements without creating another array.

def even_first(arr):
    l, r = 0, len(arr) - 1  # l = even, r = odd

    while l < r:
        while (arr[l]) % 2 == 0 and l < r:
            l += 1
        while (arr[r]) % 2 == 1 and l < r:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r = r - 1


list1 = [2, 3, 1, 4, 5, 6]

print(even_first(list1))
print(list1)


# Increment a Number
# Write a program that takes as input an array of digits encoding a nonnegative decimal
# integer D and updates the array to represent the integer D + 1.

def inc_num(arr):
    ind = len(arr) - 1
    while ind >= 0 and arr[ind] == 9:
        arr[ind] = 0
        ind -= 1
    if ind < 0:
        arr.insert(0, 1)
    else:
        arr[ind] += 1


list2 = [1, 2, 9]  # output [2, 3, 0]
inc_num(list2)
print(list2)

