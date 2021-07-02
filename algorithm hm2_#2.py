#Unique Characters in String
#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.
#Hint: https://www.w3schools.com/python/python_sets.asp

def uni_char(s):
    chars = set()

    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True


print(uni_char("abcde")) #True
print(uni_char("aabcde")) #False