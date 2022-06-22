# Selection Sort
# Implement the selection sort algorithm that is sorting in descending order

# def select_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] > arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
#
#
# list1 = [12, 4, 2, 14, 7, 9, 13]  # [2, 4, 7, 9, 12, 13, 14]
# print(list1)
# print(select_sort(list1))


# Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):  # decrement - i - 1 to not go over previous elements
#             if arr[j] < arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
#
# list2 = [4, 1, 6, 3, 5, 9]
# print(list2)
# print(bubble_sort(list2))


# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key > arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr


# list3 = [9, 3, 5, 1, 7, 2, 8]
# print(list3)
# print(insertion_sort(list3))


# Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arr(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge_arr(l_arr, r_arr):
    merged_arr = []
    i = j = 0

    while i < len(l_arr) or j < len(r_arr):
        if i == len(r_arr):
            merged_arr.append(r_arr[j])
            j += 1
            continue
        if j == len(l_arr):
            merged_arr.append(l_arr[i])
            i += 1
            continue

        if l_arr[i] >= r_arr[j]:
            merged_arr.append(l_arr[i])
            i += 1
        else:
            merged_arr.append(r_arr[j])
            j += 1
    return merged_arr


list4 = [12, 9, 4, 2, 6, 15, 3, 8]
print(list4)
print(merge_sort(list4))
