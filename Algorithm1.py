import math
from random import randint

# Swap two variables

# time complexity
'''a = int(input('input value a: '))
b = int(input('input value b: '))
print(f'a = {a}, b = {b}')

temp = a
a = b
b = temp

print(f'a = {a}, b = {b}')'''

'''''
# Factorial is displayed for user input

number = int(input('Enter a number: '))
result = 1

# Use a for loop to iterate

# for i in range(1, number +1):
#    result *= i


result = math.factorial(number)

print(f'Result: {result}')'''


# Sum of three numbers


'''random_num = randint(100, 999)
result = 0
print(f'Result: {random_num}')
# use for loop

#for digit in str(random_num): # converts random number into a string then adds each number 273 -> 2+7+3
#    result += int(digit)

while random_num != 0:
    result += (random_num % 10)
    random_num = random_num // 10
print(f'Result: {result}')'''

'''#leap year

year = int(input("Choose a year to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is NOT a leap year')
    else :
        print(f'{year} is a leap year')
else:
    print(f'{year} is NOT a leap year')'''

# Fibonacci Sequence

fib_number = int(input('Provide a number: '))
index = 3
fib_1 = 1
fib_2 = 1
result = [fib_1, fib_2]

while index <= fib_number:
    result.append(fib_1+fib_2)
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    index += 1

print(result)


