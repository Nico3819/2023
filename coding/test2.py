x = input ('enter a number:  ')
x = int(x)

for r in range (1,x+1):
  for c in range (1,x+1):
    if r <= c:
      print (r, end = "")
  print ('')    
