# order the numbers based on being Odd or Even
# def Even_First(arr):
#     even_ele, odd_ele = 0, len(arr)-1
#     while even_ele < odd_ele:
#         if arr[even_ele] % 2 ==0:
#             even_ele+=1
#         else:
#             arr[even_ele], arr[odd_ele]= arr[odd_ele], arr[even_ele]
#             odd_ele-=1
#     return arr

test_list1= [56, 23, 12, 4, 0, 43]
test_list2= [9, 9, 9]

print(test_list2)
# print(Even_First(test_list))


#Increment a number

def increment_a_number(arr):
    arr[-1]+=1
    for x in reversed(range (1, len(arr))):
        if arr [x]!= 10:
            break
        arr[x]=0
        arr [x-1]+=1

    if arr[0]== 10:
        arr[0]= 1
        arr.append(0)

    return arr



print(increment_a_number(test_list2))