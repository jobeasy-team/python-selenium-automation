#Split in Half
#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_half(string):
    length = len(string)
    halfpart = length // 2
    additional = 0
   if length % 2:
        additional=1
    leftpart = string[:halfpart+additional]
    rightpart = string[halfpart+additional:]
    return rightpart+leftpart

example='bbbbbcaaaaa'
print(split_half(example))

#*******************************************************************************************************

#Unique Characters in String
#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.

def unique_characters_check(string):
    if len(string)==1:
        return True
    character_set = set()
    for letter in string:
        if letter in character_set:
            return False
        else:
            character_set.add(letter)

    return True

sample1 = 'abcde'
sample2 = 'aabcde'
print(sample1)
print(f'abcde is unique:', unique_characters_check(sample1))
print(sample2)
print(f'aabcde is unique:', unique_characters_check(sample2))








