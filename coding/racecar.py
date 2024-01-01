import random
import time
choice = input('choose team a, b, or c:  ')

#if choice == 'a':
 
print ('===================================================')
x = 0
timea = 0
while x < 20:
  b = random.randint(1,3)
  x = x + b
  for w in range (0,b):
    print ('')
  timea = timea + 1
  print ('*')
  
a = timea
print ('team A got %s seconds' % timea)

print ('===================================================')

x = 0
y = 0
timeb = 0
while x < 20:
  list = ['*']
  b = random.randint(1,3)
  x = x + b
  for x in list:
    print (x, end = '')
    list.append('*')
   # print (b' ', end = '')
  #for q in range(0,b):
 #   print ('', end = '')
#    print ('*', end = '')
  timeb = timeb + 1
  #print ('*', end = '')

print ('')
print ('team B got %s seconds' % timeb)
b = timeb

print ('===================================================')
x = 0
timec = 0
while x < 20:
  b = random.randint(1,3)
  x = x + b
  for e in range(0,b):
    print ('')
  timec = timec + 1
  print ('*')



print ('team C got %s seconds' % timec)
c1 = timec


print ('===================================================')
print ('team a got %s ' % timea)
print ('team b got %s ' % timeb)
print ('team c got %s ' % timec)
if timea <= timeb and timea <= timec:
  print ('team A won')
elif timeb <= timea and timeb <= timec:
  print ('team B won')
elif timec <= timea and timec <= timeb:
  print ('team C won')
