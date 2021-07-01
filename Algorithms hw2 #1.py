#Split in Half.
#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’. #Anagram #Reverse String



str1 = 'aaaabbbb'
str2 = 'aaaaabbbb'
str3 = 'aaabbbb'

def string_swap(str):
    if str1:

        print(str[len(str) // 2:L] + str[0:(len(str) // 2)])

    if str2:
        print(str[len(str) // 2 + 1: len(str)] + str[0:(len(str) // 2 + 1)])

    else:
        print(str[len(str) // 2: len(str)] + str[0: len(str) // 2])

        print(str1, str2, str3)





