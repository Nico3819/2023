x = input('enter a number:  ')
x = int(x)

def display_month(x):
  if x == 1:
    print ('january')
  elif x == 2:
    print ('febuary')
  elif x == 3:
    print ('march')
  elif x == 4:
    print ('april')
  elif x == 5:
    print ('may')
  elif x == 6:
    print ('june')
  elif x == 7:
    print ('july')
  elif x == 8:
    print ('august')
  elif x == 9:
    print ('september')
  elif x == 10:
    print ('october')
  elif x == 11:
    print ('november')
  elif x == 12:
    print ('december')
  else:
    print ('type a number 1-12')
  return
  
display_month(x)
