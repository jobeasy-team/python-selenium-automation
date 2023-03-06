
def sum_of_digits(n:int):
    sum = 0
    while(n!=0):
        digits = n%10
        sum += digits
        n = n//10
    return sum


number = input("Enter a number\n")

sum = sum_of_digits(int(number))

print(f"Sum of all digits in a number {number} is {sum}")