list = []
length = 5
for x in range (0,length):
  num = input('Enter a number:  ')
  list.append(num)

def rotate(list, length):
  list1 = list[:]
  z = list1[length-1]
  for y in range (length-1, 0, -1):
    list1[y] = list1 [y-1]
  list1[0] = z 
  print (list1)

def reverse(list, length):
    list2 = []
    for q in range (length-1, -1, -1):
        list2.append(list[q])
    print (list2)    


rotate(list, length)
reverse(list, length)

