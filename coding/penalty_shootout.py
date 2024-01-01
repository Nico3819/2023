import os
import random

def goal():
  print ('                                                                     ')
  print ('=====================================================================')
  print ('||1                             2                                 3||')
  print ('||                                                                 ||')
  print ('||-----------------------------------------------------------------||')
  print ('||                                                                 ||')
  print ('||4                             5                                 6||')
  print ('||-----------------------------------------------------------------||')
  print ('||                                                                 ||')
  print ('||7                             8                                 9||')
  print ('                                                                     ')
  return

while True:
  goal()
  
  shot = input('enter a number to shoot or exit:  ')
  if shot == 'exit':
    break
  shot = int(shot)
  keeper = random.randint(1,9)

  if keeper == shot:
    os.system('banner save')
  elif shot > 9 or shot < 1:
    os.system('banner miss')
  else:
    os.system('banner goal')
