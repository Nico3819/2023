a = input('enter a calculation:  ')
x = input('enter a number:  ')
y = input('enter a number:  ')
x = int(x)
y = int(y)

def add(x,y):
  print (x + y)
  return

def subtraction(x,y):
  print (x - y)
  return

def multiplication(x,y):
  print (x*y)
  return

def division(x,y):
  print (x/y)
  return

if a == 'add':
  add(x,y)
elif a == 'subtract':
  subtraction(x,y)
elif a == 'multiply':
  multiplication(x,y)
elif a == 'divide':
  division(x,y)
