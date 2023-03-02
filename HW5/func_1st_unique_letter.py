def find_unique_letter(str):
    for i in range(len(str)):
        if (i == 0 and str[i] not in str[i + 1:]) or \
                (i > 0 and str[i] not in str[i + 1:] and str[i] not in str[:i]):
            return str[i]
            break
        elif i == len(str) - 1:
            return ""


string = input("Enter a string\n")
unique_letter = find_unique_letter(string)
if unique_letter == "":
    print("There is no unique letter in the string")
else:
    print("The first unique letter is  " + unique_letter)
