x = input('Enter a number:  ')
x = int(x)
c = -1
e = ('*')+(x-2)*(' ')+('*')
print (e)
cou = x-2

for w in range (0,x-1):
  c = c + 1
  z = ('*')+c*(' ')+('*')+(cou-1)*(' ')+('*')
  if w == x-2:
    z = ('*')+c*(' ')+('*')+(cou-1)*(' ')
  print (z)
  cou = cou - 1
