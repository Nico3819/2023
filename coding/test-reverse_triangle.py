x = input('Enter a number:  ')
x = int(x)
q = 1
z = x

for q in range(1, x+1):
  for w in range(1,z+1):
    print (w, end = "")
  q = q + 1
  z = z - 1
  print ("")
