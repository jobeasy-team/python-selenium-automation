#Count Characters
#Create a program that will count vowels and consonants in a string.
#Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}

string = input("Enter Your String : ")

vowels = consonants = 0

vowels_list = ['a', 'e', 'i', 'o', 'u']

for i in string:

    if i in vowels_list:
        vowels += 1

    if i not in vowels_list:
        consonants += 1


print("Number of Vowels in this String = ", vowels)

print("Number of Cons"
      "onants in this String = ", consonants)