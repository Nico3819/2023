list1 = []
for x in range(0,8):
  items = input('Enter a number:  ')
  items = int(items)
  list1.append(items)

num = input('Enter a number to go forth and back:  ')
num = int(num)  


def for_loop(num,list1):
  y = 0
  for x in list1: 
    if x == num:
      for q in range (0,5):
        if y < 0:
          print (list1[y])
        y = y + 1
      break  
    y = y + 1


def new_loop(num,list1):
  index = 0
  for x in list1:
    if x == num:
      break
    index = index + 1  

  if index >= 2 and index <= 5:
    for q in range(index-2,index+3):
      print (list1[q])
  elif index == 6:
      for q in range(index-2,index+2):
        print (list1[q])
  elif index == 7:
      for r in range (index-2,index+1):
        print (list1[r])  
  elif index == 1:
    for w in range(index-1,index+3):
      print (list1[w])
  elif index == 0:
    for e in range(index,index+3):
      print (list1[e])
  else:
    print ('Not in the list')  

#for_loop(num,list1)
new_loop(num,list1)
