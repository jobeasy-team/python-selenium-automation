

n = int(input("Enter a number\n"))
odd = 0
even = 0

while (n != 0):
    digit = n % 10
    if (digit % 2 == 0):
        even += 1
    else:
        odd += 1

    n = n // 10

print(f"Odd numbers are {odd}")
print(f"Even numbers are {even}")


