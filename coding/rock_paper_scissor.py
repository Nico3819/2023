def check(random,choice):
  if random == 'paper' and choice == 'rock':
    print ('you lose')
  if random == 'paper' and choice == 'paper':
    print ('you tie')
  if random == 'paper' and choice == 'scissor':
    print ('you win')
  if random == 'rock' and choice == 'paper':
    print ('you win')
  if random == 'rock' and choice == 'rock':
    print ('you tie')
  if random == 'rock' and choice == 'scissor':
    print ('you lose')
  if random == 'scissor' and choice == 'scissor':
    print ('you tie')
  if random == 'scissor' and choice == 'rock':
    print ('you win')
  if random == 'scissor' and choice == 'paper':
    print ('you lose')


while True:
  import random
  choice = input('enter rock, paper, or scissor:  ')
  if choice == 'exit':
    break
  
  list = ['rock','paper','scissor']
  random = random.choice(list)
  print (random)
  
  check(random,choice)
