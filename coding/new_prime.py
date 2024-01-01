number = input('Enter a number:  ')
number = int(number)
list = []

for x in range(1,number+1):
  list.append(x)

list2 = []

for x in list:
  if x%2 != 0 and x%3 != 0 and x%5 != 0 and x%7 != 0 and x%11 != 0:
    list2.append(x)
  if x == 2  or x == 3 or x == 5 or x == 7 or x == 11:
    list2.append(x)

print (list2)
