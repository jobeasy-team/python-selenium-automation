'''
Reverse a Statement
Build an algorithm that will print the given statement in reverse.
Example: Initial string = Everything is hard before it is easy
Reversed string = easy is it before hard is Everything
'''

def reverse_statement(string):
    result = string.split()

    print(result)
    print(result[::-1])

reverse_statement('Everything is hard before it is easy')

'''
Permutations
Write a solution that will print all permutations of a string.
A permutation is an act of changing the arrangement of characters.
Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}
'''

'''
Count Characters
Create a program that will count vowels and consonants in a string.
Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}
'''

def count_chars(string1):
    string1 = string1.replace(' ', '')
    vowel_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    vowels = 0
    consonants = 0
    for char in string1:
        if char in vowel_list:
            vowels += 1
        else:
            consonants += 1
    print(f'Vowel count = ' + str(vowels))
    print(f'Consonant count = ' + str(consonants))

count_chars('hello world')
    
