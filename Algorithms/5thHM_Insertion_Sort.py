#Insertion sort descending

def insertion_descending(arr):
    for x in range (1, len(arr)):
        value= arr[x]
        y=x-1
        while y>=0 and value > arr[y]:
            arr[y+1] = arr[y]
            y-=1
            arr[y+1]=value
    return arr

test_arr= [45,3,12,67,54,2, 17]
print(insertion_descending(test_arr))
