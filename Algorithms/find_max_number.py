def find_max_number(x, y, z):
    if x > y and x > z:
        max = x
    elif y > x and y > z:
        max = y
    else:
        max = z

    return max


print("Enter any 3 numbers:")
a = int(input())
b = int(input())
c = int(input())
print(f"Maximum number between {a} , {b} , and {c} is {find_max_number(a, b, c)}")
