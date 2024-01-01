while True:
  c = 0
  word = input('Enter a word or enter exit to quit:  ')
  if word == 'exit':
    exit()
  list = []
  list2= []
  new_word1 = ''
  for x in word:
    list.append(x)
  if list[0] == 'a' or list[0] == 'e' or list[0] == 'i' or list[0] == 'o' or list[0] == 'u': 
    print (word+'way')
    print ('')
  else:
    for x in word:
      if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        break
      else:
        c = 1
        list2.append(x)
        new_word1 = (new_word1+x)
        new_word = word.replace(x,'')
  new_word = word.replace(new_word1,'')

  if c == 1:
    print (new_word+new_word1+'ay')
    print ('')
