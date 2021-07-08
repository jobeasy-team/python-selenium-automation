#Permutations
#Write a solution that will print all permutations of a string.
#A permutation is an act of changing the arrangement of characters.
#Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}

def permutate_string(string, prefix = ''):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i+1:]
            permutate_string(rem, prefix + string[i])
permutate_string('ABC')