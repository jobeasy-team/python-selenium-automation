#Посчитайте, сколько раз символ встречается в строке. Строка и символ вводятся с клавиатуры. DON’T USE METHOD COUNT
def symbolInString():
    string = input('Enter a string:')
    symbol = input('Enter a symbol that you want to search for:')

    frequency = 0
    for letter in string:
        if letter == symbol: frequency += 1

    return frequency