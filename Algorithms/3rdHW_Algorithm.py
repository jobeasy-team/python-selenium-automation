# using some built-in functions
# def less_than_arith_mean(lst):
#     arith_mean=sum(lst)/len(lst)
#     less=[]
#     print(arith_mean)
#     for x in lst:
#         if x <arith_mean:
#             less.append(x)
#             print(less)

#without built-in functions
def less_than_arith_mean(lst):
    arith_mean=sum(lst)/len(lst)
    less=[]
    print(arith_mean)
    for x in lst:
        if x <arith_mean:
            less.append(x)
            print(less)


test_list=[1,4,6,7,8]

print(less_than_arith_mean(test_list))