x = input('enter a number:  ')
y = input('enter a number:  ')
x = int(x)
y = int(y)
guess = input('enter the answer:  ')
guess = int(guess)

def correct(x,y,guess):
  answer = (x * y)
  if guess == answer:
    print ('that is the correct answer')
  else:
    print ('that is the wrong answer')
correct(x,y,guess)
