while True:
  word = input('enter a word:  ')
  if word == 'exit': 
    break
  le = len(word)
  le = le - 1
  list = []
  for x in word:
    list.append(x)
  letter = (list[le])
  if letter == 'g' or 'k' or 'y':
    final = word + 'ing'
    print (final)
  else:
    print ('cannot be a conjugation')
