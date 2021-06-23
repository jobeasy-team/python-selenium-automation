n = int(input('Enter a number:'))

while n <= 1:
    n = int(input('Please input a new number'))

total = 0
my_sum = 0
while (n - 1) >= total:
    total = total + 1
    my_sum += total
    print(my_sum)
