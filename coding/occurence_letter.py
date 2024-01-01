letter = input('Enter a letter:  ')
word = input('Enter a word:  ')

def letter_occurence(letter, word):
  cou = 0
  for x in word:
    if x == letter:
      cou = cou + 1
  print (cou)
letter_occurence(letter, word)
