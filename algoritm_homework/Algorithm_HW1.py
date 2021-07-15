def sum(n):
    result = 0
    if n > 0:
        for i in range(1, n + 1):
            result += i
    print(f'The sum of positive integers up to {n} is {result}')

#number = int(input('Input number: '))
#sum(number)

#------------------------------------------------------------------------------------------------------------------
def find_max_number(list):
    list = []
    max = 0

    a = input('Input number a: ')
    list.append(a)
    b = input('Input number b: ')
    list.append(b)
    c = input('Input number c: ')
    list.append(c)

    for i in list:
        if int(i) > max:
            max = int(i)
    print(f'The highest number is: {max}')

#find_max_number(list)

#------------------------------------------------------------------------------------------------------------------
def count_odd_even(number):
    odd = 0
    even = 0
    for i in number:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'There are {odd} odd digits and {even} even digits in {number}.')
    
#number = input('Input a number with at least 5 digits: ')
#count_odd_even(number)


