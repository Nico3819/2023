li = []

while True:
  x = input('enter a name: ')
  if x == 'exit':
    break
  else:
    li.append(x)

print (li)
x = len(li)
x = x - 1
while x > -1:
  print (li[x])
  x =  x - 1
