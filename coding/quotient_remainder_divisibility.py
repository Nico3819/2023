x = input('enter a number:  ')
y = input('enter a number:  ')
x = int(x)
y = int(y)

def quotient_remainder(x,y):
  answer = (x // y)
  remainder = (x % y)
  print ('quotient = %s' % answer)
  print ('remainder = %s' % remainder)

quotient_remainder(x,y)
