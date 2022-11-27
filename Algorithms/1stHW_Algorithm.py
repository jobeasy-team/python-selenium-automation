# def sum_digits(num):
#     result=0
#     for x in range (1, num+1):
#         result = result + x
#     return result
#
# print(sum_digits(100))


# # max value
# def max_num (a, b, c):
#     max_val = 0
#     if a> b and a>c:
#         max_val = a
#     if b>a and b>c:
#             max_val = b
#     else: max_val = c
#     return max_val

# print(max_num(67, 34, 5676))


# count odd and even

def count_odd(a):
    odd_num = 0
    even_num=0

    while a > 0:
        num = a % 10
        if num % 2:
           even_num+=1
        else:
            odd_num =+1
        a = a// 10

    return [even_num,odd_num]

print(count_odd(4532))