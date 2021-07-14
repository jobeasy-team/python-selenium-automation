'''
Split in Half
Given a string. Split it into two equal parts. Swap these parts and return the result.
If the string has odd characters, the first part should be one character greater than the second part.
Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.
'''

def split_in_half(string):
    length = len(string)
    half = length // 2
    mod = 0
    if length % 2 == 0:
        mod = 1
    first = string[:half + mod]
    last = string[half + mod:]
    return last + first

print(split_in_half('aaccbb'))

'''
Unique Characters in String
Given a string, determine if it consists of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.
'''
def unique_char(string1):
    set1 = set(string1)
    return len(string1) == len(set1)

print(unique_char('abcde'))
print(unique_char('aabcde'))


