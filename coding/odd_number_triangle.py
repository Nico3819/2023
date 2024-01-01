x = input('Enter a number:  ')
x = int(x)

for r in range (1,x+1):
  z = 1
  h = 0
  while z < 20:
    if h < r:
      if z % 2 == 1:
        print (z,end='')
        h = h + 1
    else:
      break
    z = z + 1
  print ('')
