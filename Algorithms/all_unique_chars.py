def unique_chars(s):
    for i in range(len(s)-1):
        if s[i] in s[i+1:]:
            return False
    return True


print(unique_chars('aabcde'))