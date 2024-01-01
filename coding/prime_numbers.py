number = input('Enter a number:  ')
number = int(number)
list = []

for x in range(0,number+1):
  list.append(x)
count = -1
for x in list:
  count = count + 1
  if list[count]%2 == 0:
    list.remove(count)
  if list[count] == 0: 
    list.remove(count)
  if list[count] == 0:
    list.remove(count)
  if list[count] == 0:
    list.remove(count)

print (list)
