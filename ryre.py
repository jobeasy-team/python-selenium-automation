def anagram(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s1.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for l in s1:
        if l in count:
            count[l] = count[l] + 1
        else:
            count[l] = 1

    for l in s2:
        if l in count:
            count[l] = count[l] - 1
        else:
            count[l] = 1

    for k in count:
        if count[k] != 0:
            return False

        return True


print(anagram('anagram', 'nagaram'))