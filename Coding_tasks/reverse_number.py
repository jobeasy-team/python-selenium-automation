number = 12345
reversed_array = []

while number != 0:
    x = number % 10
    reversed_array.append(x)
    number = number // 10

print(reversed_array)
