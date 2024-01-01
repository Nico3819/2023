import time
import random

print ('')
print ('====================================================')
lista = []
listb = []
listc = []

dicea = random.randint(1,3)
diceb = random.randint(1,3)
dicec = random.randint(1,3)

ta = 0
tb = 0
tc = 0
cou = 0
a = 0
b = 0
c = 0

while ta < 20 or tb < 20 or tc < 20:
  dicea = random.randint(1,3)
  diceb = random.randint(1,3)
  dicec = random.randint(1,3)
  a = a + 1
  b = b + 1
  c = c + 1
  cou = 0
  while cou < dicea:
    lista.append('*')
    cou = cou + 1
  cou = 0
  while cou < diceb:
    listb.append('*')
    cou = cou + 1
  cou = 0
  while cou < dicec:
    listc.append('*')
    cou = cou + 1
  print ('')
  print ('Team A %s points' % ta) 
  print (''.join(lista))
  print ('')
  print ('Team B %s points' % tb)
  print (''.join(listb))
  print ('')
  print ('Team C %s points' % tc)
  print (''.join(listc))
  print ('')
  cou = cou + 1
    #if c == dice:
      #print (''.join(list))
  ta = dicea + ta
  tb = diceb + tb
  tc = dicec + tc
#  print (list)
  print ('==================================================')
  time.sleep(0.5)
  if ta > 21:
    if ta == tb:
      print ('Team A and Team B tied with %s points' % ta)
      print ('Team C got %s points' % tc)
      break
    elif ta == tc:
      print ('Team A and Team C tied with %s points' % ta)
      print ('Team B got %s points' % tb)
      break
    else:
      print ('Team A won')
      print ('Team A got %s points' % ta)
      print ('Team B got %s points' % tb)
      print ('Team C got %s points' % tc)
      break
  elif tb > 21:
    if tb == ta:
      print ('Team B and Team A tied with %s points' % tb)
      print ('Team A got %s points' % ta)
      break
    elif tb == tc:  
      print ('Team B and Team C tied with %s points' % tb)
      print ('Team A got %s points' % ta)
    else:
      print ('Team B won')
      print ('Team B got %s points' % tb)
      print ('Team A got %s points' % ta)
      print ('Team C got %s points' % tb)
      break
  elif tc > 21:
    print ('Team C won')
    print ('Team C got %s points' % tc)
    print ('Team A got %s points' % ta)
    print ('Team B got %s points' % tb)
    break
