x = input('Enter a number:  ')
x = int(x)

for r in range (1,x+1):
  print (r)
  if r < x:
    for c in range (1,r+1):
          print (c, end = "")

