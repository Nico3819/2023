while True:
  print ("=================================")
  x = input('enter a word:  ')
  # print ("=================================")
  if x == 'exit':
    break
  le = len(x)
  list = []
  for a in x:
    list.append(a)
  y = le - 1
  c = y
  list2 = []
  list2.append(list[y])
  #print (list2[0])
  def plural(x):
    if list2[0] == 's':
      plural = x + 'es'
      print (plural)
    elif list2[0] == 'y':
      plural1 = x + 'ies'
      s = plural1.replace(plural1[c],'')
      print (s)
    else:
      plural2 = x + 's'
      print (plural2)
  plural(x)
