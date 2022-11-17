
test_arr= [45,3,12,67,54,2, 17]


# selection_sort descending


def selection_descending(arr):
    for x in range(len(arr)):
        max_index = x
        for y in range(x+1, len(arr)):
            if arr[y] > arr[max_index]:
                max_index = y
        arr[x], arr[max_index] = arr[max_index], arr[x]
    return arr

print(selection_descending(test_arr))