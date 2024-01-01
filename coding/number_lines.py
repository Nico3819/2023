x = input('Enter a number:  ')
x = int(x)
c = 1

lines = 0

for q in range(0,x):
  print (c)
  c = c + 1
  for w in range (0,c-1):
    if x == 1:
      break
    print (c,end = "")
  if c == x:
    print (c,end = "")
    break

print ('')
