x = input('enter an age:  ')
x = int(x)
total = input('enter the total:  ')
total = int(total)

def reduction(x):
  discount = 0
  if x < 10:
    discount = 50
    return (discount)
  elif x > 10 and x < 19:
    discount = 30
    return (discount)
  elif x > 59:
    discount = 20
    return (discount)
  else:
    print ('you get no discount')
    return (0)

my_discount = reduction (x)

def amount(total,x,discount):
  x = discount/100
  discount = total*x
  new = (total - discount)
  print ('you have to pay %s0' % new)

amount(total,my_discount,my_discount)
