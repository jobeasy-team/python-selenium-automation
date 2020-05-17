#Write a Python program to get the largest number from a list.

#list = [1,4,5,3,12,0,345,13252]
#print("Largest number from the list is :", max(list))



#Input your age. If you are 18 or over, print the message “You can vote”, if you are aged 17, print the message “You can learn to drive”, if you are 16, print the message “You can buy a lottery ticket”, if you are under 16, print the message “You can go Trick-or-Treating”

#Age = int(input("Your age: "))
#if Age > 18:
#    print ("You can vote"),
#if Age == 17:
#    print ("You can learn to drive"),
#if Age == 16:
 #   print ("You can buy a lottery ticket"),
#if Age < 16:
#    print ("You can go trick-or-treating")


#Enter a random string, which includes only digits. Write a function sum_digits which will find a sum of digits in this string

digits = '11,22,123,455'
def sum_digits(string_n):
    sumofdigitsinstring_n = 0
    for currentdigitasastring in string_n:
        currentdigitsasanInt = int(currentdigitasastring)
        sumofdigitsinstring_n = sumofdigitsinstring_n + currentdigitsasanInt
    return sumofdigitsinstring_n


