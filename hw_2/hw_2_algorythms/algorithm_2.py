# Посчитать четные и нечетные цифры числа. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def oddEven(num):
    # return a map, having two keys:
    # Example: num = 34560
    # {
    # "odd" : 2,
    # "even" : 3
    # }

    resultMap = {
        "odd": 0,
        "even": 0
    }
    if num == 0:
        resultMap["even"] += 1
        return resultMap

    # take care of negative input
    if num < 0:
        num = 0 - num

    # iterate over the number and count even and odd digits
    while (num > 0):
        digit = num % 10
        num = num // 10
        if digit % 2 == 0:
            resultMap["even"] += 1
        else:
            resultMap["odd"] += 1

    return resultMap