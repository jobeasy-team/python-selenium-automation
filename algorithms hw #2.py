#Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.


#num1 = float(input("124"))
#num2 = float(input("21"))
#num3 = float(input("32"))

#if (num1 > num2) and (num1 > num3):
#   largest = num1
#elif (num2 > num1) and (num2 > num3):
#   largest = num2
#else:
#   largest = num3

#print("The largest number is",largest)

# 0(1)
def find_max(a, b, c):
      if a > b and a > c:
         return a
      if b > a and b > c:
         return b
      return c


n1 = int(input("Input first num: "))
n2 = int(input("Input second num: "))
n3 = int(input("Input third num: "))

print(find_max(n1, n2, n3))

