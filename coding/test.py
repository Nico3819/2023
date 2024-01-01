number = input('Enter a number:  ')
number = int(number)
list = []

for x in range(1,number+1):
  list.append(x)

print(list)

list.remove(1)
print (list)
