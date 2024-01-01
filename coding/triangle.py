x = input('Enter a number:  ')
x = int(x)

c1 = x - 1
lines = 0

while c1 < x:
  if lines == x:
    break
  print ('*')
  lines = lines + 1
  c1 = 0
  while c1 < lines:
   if lines == x:
     break
   c1 = c1 + 1
   print ('*', end = '')
print ('')
print (lines)
