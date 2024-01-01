x = input('Enter a number:  ')
x = int(x)
c = 0

for q in range(0,x):
  for w in range (0,x):
    if q == 0 or q == x-1:
      print ('*', end = "")
    else:
      print('*', end = " "*(x-2))
      c = c + 1
      if c == 2:
        c = 0
        break
  print ('')
