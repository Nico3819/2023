def greeting():
  while True:
      x = input('enter a name or exit:  ')
      if x == 'nico' or x == 'leo' or x == 'mayur' or x == 'daniela':
        print ('hello')
      elif x == 'exit':
        break
      else:
        print ('i don\'t know you')

greeting() 
