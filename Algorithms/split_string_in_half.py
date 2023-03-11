def split_in_half(s):
    first_half = ''
    second_half = ''
    middle = 0

    if len(s) %2 ==0:
        middle = len(s)//2
    else:
        middle = len(s)//2 + 1

    first_half = s[:middle]
    second_half = s[middle:]

    return second_half + first_half


print(split_in_half('bbbbbcaaaaa'))