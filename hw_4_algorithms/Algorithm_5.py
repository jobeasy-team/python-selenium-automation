#Возведение в степень рекурсией

def exponentOfANumber(number, exponent):
  if number == 0: return 0
  if exponent == 0: return 1
  if exponent == 1: return number

  return number * exponentOfANumber(number, exponent-1)