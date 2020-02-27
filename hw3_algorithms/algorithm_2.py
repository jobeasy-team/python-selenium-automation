def longestWord():
  sentence = input('Please enter a sentence with words separated by spaces:')
  words = sentence.split()

  if len(words) == 0: return ""
  if len(words) == 1: return words[0]

  longest = ""
  for word in words:
    if len(word) > len (longest): longest = word

  return longest