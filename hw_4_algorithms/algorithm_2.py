#В строке найти и заменить одну подстроку на другую. Если одинаковых подстрок несколько, заменить все. Строка, значение которое надо заменить и значение, на которое надо заменить вводятся с клавиатуры. DON’T USE METHOD REPLACE
def findAndReplace():
  string = input('Enter a string:')
  find = input('Enter string to find and replace:')
  replace = input('Enter the replacement:')

  otherParts = string.split(find)
  return replace.join(otherParts)