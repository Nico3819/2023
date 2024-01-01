list = []
for q in range(0,5):
  x = input('Enter a number:  ')
  x = int(x)  
  list.append(x)

for x in range (0,4):
  for x in range (0,4):
    if list[x] > list[x+1]:
      s = list[x]
      list[x] = list[x+1]
      list[x+1] = s
    print (list)
    
  

print (list)
