#Reverse a Statement
#Build an algorithm that will print the given statement in reverse.
#Example: Initial string = Everything is hard before it is easy
#Reversed string = easy is it before hard is Everything

string = "Everything is hard before it is easy"

words = string.split()

words = list(reversed(words))

print(" ".join(words))