x = input('Enter a number:  ')

x = int(x)
c = x

for q in range(1,x+1):
  for w in range(1,c+1):
    print (c, end = "")
  c = c - 1
  print ('')
