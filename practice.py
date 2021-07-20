#word = 'Just do it!'
#print(word[10])
#print(word[5:7])
#print(word[7:10])
#print(word[4:])

#(strings)
#ex_1 = False
#ex_2 = str(29)
#ex_3 = 4.1352

#print(type(ex_1))
#print(type(ex_2))
#print(type(ex_3))

#ex_4 = 24.1
#print(type(ex_4))


#ex_6 = str(25.3)
#print(type(ex_6))

#print("This\tis\ta\ttest")
#print("this line\nthis line2")
#print("When I said \'immediately,\' I meant today!")
#print('This a test \\')


#name = input("What is your name? ")
#quest = input("What is your quest? ")
#Favorite_color = input("What is your favorite color? ")

#print("So your name is " + name + ", your quest is " + quest)

#int_num = input("Please enter your number ")

#print(bool(int_num) +10)

#def name_printer():
#    print('name')

#name_printer()

#print("  *******\n   *****\n    ****\n     **\n      *")


my_list = [21, 12, 12, 4]
print(min(my_list))

li = []
n = int(input("Enter the number of elements: "))
for i in range(1, n+1):
    elem = int(input("Enter the elements: "))
    li.append(elem)
li.sort()

print("The sorted list: ", li)
print("The second smallest value of this list: ",li[1])

def unique_in_order(iterable):
    iterable= list(set(iterable))

    return sorted(iterable)