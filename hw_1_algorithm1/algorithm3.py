#create a random number in a range (rewrite a program with any number of digits. Instead of 3 digits, you should sum digits up from n digits number.
#user enters n manualy (n>0)
from random import randint

n = int(input("Enter a number of digits: "))

def sum_of_digits(digits):
    if digits < 1:
        print ("Wrong value. The number should have at least 1 digit.")
        quit()
    down = 10 ** (digits - 1)
    up = 10 ** digits - 1
    n = randint(down, up)
    print(f'We got the number {n}')

    result = 0
    i = 0
    while i < digits:
        result += n % 10
        n = n // 10
        i += 1
    print(f'The result is {result}')

 sum_of_digits()


