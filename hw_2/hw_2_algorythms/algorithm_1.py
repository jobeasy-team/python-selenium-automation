num 1 = int(input(f"first number"))
num 2 = int(input(f"second number"))
num 3 = int(input(f"third number"))

def max_of_three(num1,num2,num3):
    if num1 > num2:
        if num1 > num3:
            print(f"The biggest of the numbers {num1}, {num2}, {num3} is {num1}")
        else:
            print(f"The biggest of the numbers {num1}, {num2}, {num3} is {num3}")
