"""
Selection Sort
Implement the selection sort algorithm that is sorting in descending order.
"""

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#
#     return arr
#
# test_data = [7, 3, 5, 6, 4, 10, 3, 2]
# print(test_data)
#print(selection_sort(test_data))

"""
Bubble Sort
Implement the bubble sort algorithm that is sorting in descending order.
"""

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# test_data = [7, 3, 5, 6, 4, 10, 3, 2]
# print(test_data)
# print(bubble_sort(test_data))

"""
Insertion Sort
Implement the insertion sort algorithm that is sorting in descending order.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

test_data = [7, 3, 5, 6, 4, 10, 3, 2]
print(test_data)
print(insertion_sort(test_data))
