word = input('Enter a word:  ')

def capital(word):  
  cou = 0
  for x in word:
    num = ord(x)
    if num > 64 and num < 91:
      cou = cou + 1
  print ('There are %s capital letters.' % cou)
capital(word)  
