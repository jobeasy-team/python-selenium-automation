#Compute the sum of digits in all numbers from 1 to n. When a user enters a number n,
#find the sum of digits in all numbers from 1 to n.
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

sum_digits = int(input('Please Input a Number: '))
result = 0
for num in range (1, sum_digits + 1):
    result = result + num
    print (f'result: {result}')

#Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.

max_value = input ("Enter 3 values seperated by a space: ")
result = max_value.split()
y = max(result)
print (y)

#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
num_list = [3, 4, 5, 6, 0]
even = []
odd  = []
for i in num_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)