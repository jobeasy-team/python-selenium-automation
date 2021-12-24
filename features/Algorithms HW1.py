#Note: ALL 3 ANSWERS GATHERED IN A SINGLE FILE BUT THEY WORK INDIVIDUALLY...

# Compute the sum of digits in all numbers from 1 to n.
# When a user enters a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

n=int(input('input value n:'))

result=0
if n != 0:
    for i in range(n+1):
       result=result+i
   print(f'The sum of digit in all numbers from 1 to n is:{result}')

##################################################################################################################

 Find max number from 3 values, entered manually from a keyboard.
 Example: 124, 21, 32. Result = 124.

 def max_number(x, y, z):
   list = [x, y, z]
   return max(list)

 a = int(input("Enter First number"))
 b = int(input("Enter Second number"))
 c = int(input("Enter Third number"))

print('The max number among the three is :', max_number(a,b,c))

##################################################################################################################

#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

n = int(input("Enter a number to count evens & odds:"))

x = [int(a) for a in str(n)]

even_count, odd_count = 0, 0

for i in x:
        if i % 2 == 0:
            even_count +=1
        else:
            odd_count +=1

print("Count of the even numbers: ", even_count)
print("Count of the odd numbers: ", odd_count)
