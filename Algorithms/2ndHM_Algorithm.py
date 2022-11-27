# def split_string(st):
#     half = len(st)//2
#     num = 0
#     if len(st) % 2:
#         num = 1
#
#     left = st[:half+num]
#     right = st[half:]
#     new_str = right + left
#     return new_str
#
#
# test_str = "bbbbbaaaaaccc"
# print(test_str)
# print(split_string(test_str))


def unique_char(str):
    new_str = []
    for x in str:
        if x in new_str:
            return False
        else:
            new_str.append(x)
    return True




print(unique_char("asdfk"))
