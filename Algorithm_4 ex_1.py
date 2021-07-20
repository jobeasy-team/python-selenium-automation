

def below_ar_mean(arr):
    ar_mean = sum(arr) / len(arr)
    print("Ar, mean: " +str(ar_mean))
    final_list = []
    for i in arr:
            if i < ar_mean:
                final_list.append(i)
    return final_list

test_array = [1,3,5,6,4,10,2,3]
print(test_array)
print(below_ar_mean(test_array))