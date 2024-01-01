x = input('Enter a number:  ')
x = int(x)

for q in range(1,x+1):
  for w in range (0,x-1):
    print (' ', end = "")
  x = x - 1
  print (q)
