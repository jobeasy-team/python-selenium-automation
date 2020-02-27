def findAndReplace():
  string = input('Enter a string:')
  find = input('Enter string to find and replace:')
  replace = input('Enter the replacement:')

  otherParts = string.split(find)
  return replace.join(otherParts)

#2. In a string find and replace one substring by another. If 2 similar substrings are there, replace all of them. A string which being replaced and a new meaning of it are input through keyboard. DON’T USE METHOD REPLACe