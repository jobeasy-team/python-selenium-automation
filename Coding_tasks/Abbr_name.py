name = input("Enter your name(Firstname and lastname)")
print(name)

for i in range(len(name) - 1):
    if name[i] == ' ':
        abbr = name[i + 1]
        break

print(f"The abbreviation of you name is {name[0] + '.' + abbr}")
