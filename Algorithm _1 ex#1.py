#Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 1


#n = int(input('Enter a number:'))

#while n <= 1:
#    n = int(input('Please input a new number'))

#total = 0
#my_sum = 0
#while (n - 1) >= total:
#    total = total + 1
#    my_sum += total
#    print(my_sum)


#Class solution

# 0(n)
def sum1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += final_sum + x

    return final_sum

num = int(input("Input a number: "))
print(sum1(num))

# 0(1)
def sum2(n):
    return (n * (n + 1)) / 2

num = int(input("Input a number: "))
print(sum2(num))


