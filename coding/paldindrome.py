def func():
  word = input('Enter a word or enter exit to quit:  ')
  if word == 'exit':
    exit()
  c = len(word)
  reverse = []
  word1 = []
  while c > 0: 
    reverse += word[ c - 1 ]
    c = c - 1

  for x in word:
    word1.append(x)

  #print (word1)
  #print (reverse)

  if reverse == word1:
    print ('They are a palindrome.')
  else:
    print ('They are not a palidrome')
while True:
  func()
  print ('')
