x = input('Enter a number:  ')

x = int(x)
c = 0

for q in range(1,x+1):
  for w in range(1,x+1-c):
    print (w, end = "")
  c = c + 1
  print ('')
