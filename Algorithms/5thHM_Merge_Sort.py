# Merge Sort Descending
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))



def merge_arrays (left_arr, right_arr):
    new_arr = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            new_arr.append(right_arr[j])
            j+=1
            continue
        if j == len(right_arr):
            new_arr.append(left_arr[i])
            i+=1
            continue

        if left_arr[i] >= right_arr[j]:
            new_arr.append(left_arr[i])
            i+=1
        else:
            new_arr.append(right_arr[j])
            j+=1
    return new_arr





test_list = [23,65,12,4,1,76]
print(test_list)
print(merge_sort(test_list))


