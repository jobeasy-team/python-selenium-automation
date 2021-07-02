#Split in Half.
#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’. #Anagram #Reverse String


def split_in_half(s): #aacbb
    length = len(s) #5
    half = length // 2 #2
    add = 0
    if length %2: # 1
        add = 1
    left = s[:half + add] # s[:3] aac
    right = s[half + add] # s[3] bb
    return right + left # bbaac


print(split_in_half("aacbb")) # aacbb -> bbaac
print(split_in_half("aabb")) # aabb -> bbaa

