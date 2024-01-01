list = []
for x in range (0,5):
  y = input('Enter a number:  ')
  y = int(y)
  list.append(y)
delete = input('Enter an element to delete:  ')
delete = int(delete)

def delete_element(list, delete):
  list1 = []
  for x in list:
    if x != delete:
      list1.append(x)
  print (list1)

delete_element(list,delete) 
