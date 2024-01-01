x = input('Enter a number:  ')
x = int(x)
c = 1
c2 = 2

for q in range (1,x):
  if c == x:
    break
  print (q)
  for w in range (1,x):
    if c == x:
      break
    else:
      print (c, end = "")
    
    c = c + 1

print ('')
