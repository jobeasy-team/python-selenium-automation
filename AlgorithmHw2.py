# 1
# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.

'''orig_string = "bbbbbcaaaa"

res1 = orig_string[0:len(orig_string) // 2]
res2 = orig_string[len(orig_string) // 2 if len(orig_string) % 2 == 0
                   else ((len(orig_string) // 2) + 1):]

print(res1 + res2)'''

# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

string_1 = "vnskjvnaskljval"


def unique_char(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


print(unique_char(string_1))
