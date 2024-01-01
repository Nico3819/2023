x = input('Enter a number:  ')
x = int(x)
c = 0
line = 1

for q in range(0,1):
  if x == 1:
    print ('n')
    break
  if x == 2:
    print ('nn')
    print ('nn')  
    break

for q in range(0,x):
  for w in range(1,x):
    if x == 2:
      break
    if c == 0 and line == 1:
      print ('n', end = "")
      c = c + 1
    elif c == x-2 and  line == x:
      print ('*n', end = "")
      c = c + 1
      print ('')
    elif c == 0 and line == x:
      print ('n', end = "")
      c = c + 1
    elif c == x-2 and line == 1:
      print ('*n', end = "")
      c = c + 1
      print ('')
    else:
      print ('*', end = "")
      if c == x-2:
        print ('*', end = "")
        print ('')
      c = c + 1
  c = 0
  line = line + 1
