#Write a program that takes as input an array of digits encoding a nonnegative
#decimal integer D and updates the array to represent the integer D + 1.
#For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i -1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

list = [1, 2, 9]
print(list)
print(plus_one(list))