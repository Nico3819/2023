while True:
  c = 0
  word1 = input('enter a word or enter exit to quit:  ')
  if word1 == 'exit':
    break
  word2 = input('enter a word:  ')
  
  len1 = len(word1)
  len2 = len(word2)

  if len1 == len2:
    print ('they are the same length')
    for x in word1:
      for q in word2:
        if x == q:
          c = c + 1
    print ('the words have %s of the same letters'% c)
    if word1 == word2:
      print ('they are the same word')
  else:
    for x in word1:
      for q in word2:
        if x == q:
          c = c + 1
    print ('they are not the same length')
    print ('they are not the same word')
    print ('the words have %s of the same letters'% c)
