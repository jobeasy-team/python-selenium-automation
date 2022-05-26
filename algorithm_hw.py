# Compute the sum of digits in all numbers from 1 to n.
# When a user enters a number n, find the sum of digits in all numbers from 1 to n.

# O(1)
num = int(input('Enter a random number: '))

print(sum(range(num + 1)))

# Find max number
# from 3 values, entered manually from a keyboard.

# O(log n)
max_num = []
num = int(input('How many numbers?  '))

for n in range(num):
    numbers = int(input('Enter a random number: '))
    max_num.append(numbers)
print('The max number is:', max(max_num))

# Count odd and even numbers.
# Count odd and even digits of the whole number

#O(n)
n = 334455
even = 0
odd = 0

while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
print(f'There are {even} even numbers and {odd} odd numbers')
