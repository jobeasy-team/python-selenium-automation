#Bubble Sort Descending

def bubble_descending(arr):
    n= len(arr)
    for x in range(n):
        for y in range (n - x - 1):
            if arr[y]<arr[y+1]:
                arr[y], arr[y+1]= arr[y+1], arr[y]
    return arr



test_arr= [45,3,12,67,54,2, 17]

print(bubble_descending(test_arr))