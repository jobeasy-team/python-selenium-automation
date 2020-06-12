#Find maximum number from 3 values, entered manually from the keyboard

num1 = int(input(f"First number: "))
num2 = int(input(f"Second number: "))
num3 = int(input(f"Third number: "))

def maximum_of_three(number1, number2, number3):
    if number1 > number2:
        if number1 > number3:
            print(f"The greatest number in the range is {number1}")
        else:
            print(f"The greatest number in the range is {number3}")
    else:
        if number2 > number3:
            print(f"The greatest number in the range is {number2}")
        else:
            print(f"The greatest number in the range is {number3}")

maximum_of_three(num1, num2, num3)


