# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

string = 'bbbbbcaaaaa'

first_part = string[0:len(string) // 2 if len(string) % 2 == 0
else ((len(string) // 2) + 1):]

sec_part = string[len(string) // 2:]

sec_part = sec_part[1:]

c = first_part
first_part = sec_part
sec_part = c
print(first_part + sec_part)


# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def my_unique(s):
    unique = {}

    for letter in s:
        if letter in unique:
            unique[letter] = unique[letter] + 1
        else:
            unique[letter] = 1

    for key in unique:
        if unique[key] != 1:
            return False
    return True
unique1 = 'abcde'
unique2 = 'aabcde'

print (my_unique(unique2))
print (my_unique(unique1))