while True:
  word = input('enter a word:  ')
  if word == 'exit':
    break
  a = len(word)
  a = a - 1
 
  while a > -1:
    print (word[a],end = "")
    a =  a - 1
  print ('')
