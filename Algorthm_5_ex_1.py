#Your input is an array of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input array).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]


def arrayEvenAndOdd(arr, n):
    ind = 0;
    a = [0 for i in range(n)]

    for i in range(n):
        if (arr[i] % 2 == 0):
            a[ind] = arr[i]
            ind += 1

    for i in range(n):
        if (arr[i] % 2 != 0):
            a[ind] = arr[i]
            ind += 1

    for i in range(n):
        print(a[i], end=" ")

    print()



list = [7, 3, 5, 6, 4, 10, 3, 2]
n = len(list)

arrayEvenAndOdd(list, n)
