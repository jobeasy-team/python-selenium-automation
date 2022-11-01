# >>>>>>>>>>>>>first Excersise<<<<<<<<<<<<
# using some built-in functions
# def less_than_arith_mean(lst):
#     arith_mean=sum(lst)/len(lst)
#     less=[]
#     print(arith_mean)
#     for x in lst:
#         if x <arith_mean:
#             less.append(x)
#             print(less)

# without built-in functions
# def less_than_arith_mean(lst):
#     lst_sum=0
#     lst_len=0
#     less=[]
#     for x in lst:
#         lst_sum= lst_sum+x
#     print("the sum of the list is: " f'{lst_sum}')
#
#     for l in lst:
#         lst_len+=1
#     # return lst_sum
#     lst_mean= lst_sum/lst_len
#     print('the arithmetical mean is: 'f'{lst_mean}')
#
#     for y in lst:
#         if y<lst_mean:
#          less.append(y)
#     print("the elements less than arithmetical mean are: "f'{less}')

test_list = [1, 4, 6, 7, 8]


# print(less_than_arith_mean(test_list))


# >>>>>>>>>>>>>Second Exercise<<<<<<<<<<<<

def two_small_elements(lst):
    # first i sort the numbers from lowest to highest
    for x in range(0, len(lst) - 1):
        for y in range(x + 1, len(lst)):
            if (lst[x] > lst[y]):
                lst[y], lst[x] = lst[x], lst[y]
        print("sorted list: " f'{lst}')
    # then i will print the first two elements
    if len(lst) > 3:
        print("the two smallest elements are: " f'{lst[:2]}')


print(two_small_elements(test_list))
