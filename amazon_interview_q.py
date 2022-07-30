"""
HW 5
4** Amazon interview question:
Create a function that will take a string as an input
and return the 1st unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?

How to handle ""? => return Value Error
"""

#
# def unique(string: str):
#     # Google
#     string = string.lower()  # google
#
#     for l in string:  # O(n)
#         if string.count(l) == 1:  # O(n)
#             return l
   # O(n^2)
#

# print(unique('Google'))
# print(unique('Amazon'))
# print(unique('amazon'))


def unique(string): # amazon
    string = string.lower()
    d = {}

    for letter in string: # g # O(n)
        # print('\nDict', d)
        if letter not in d:
            d[letter] = 1 # => d = {} => d= {'g': 1}
        else:
            d[letter] += 1 #  d = {'g': 1, 'o': 2}

    # {'a': 2, 'm': 1, 'z': 1, 'o': 1}
    for k, v in d.items(): # O(n)
        if v == 1:
            return k
    # O(n)
print(unique('amazon'))
print(unique('xoxoxooxxot'))
print(unique('google'))
print(unique('Google'))
print(unique('4356734543%%%%%'))
print(unique(''))
print(unique(2543256342))

