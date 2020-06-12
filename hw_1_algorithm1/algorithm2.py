#count odd and even numbers of he whole number (int)

number = int(input(f"Enter a number: "))

def count_odd_even(num):
    odd_counter = 0
    even_counter = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
        num = num // 10
    print(odd_counter)
    print(even_counter)

count_odd_even(number)
