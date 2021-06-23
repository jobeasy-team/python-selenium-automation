#Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.


num1 = float(input("124"))
num2 = float(input("21"))
num3 = float(input("32"))

if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3

print("The largest number is",largest)