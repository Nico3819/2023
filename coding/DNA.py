dna = input('Enter a DNA sequence whose characters are among A,C,T,G:  ')


# Calling function presence_of_a()

def presence_of_a(dna):
  a = 0
  for x in dna:
    if x == 'a':
      a = 1
    else:
      x = 0
  if a == 1:
    print ('True sequence')
  if a == 0:
    print ('False sequence')


# Calling function presence_of_a()
presence_of_a(dna)



# Defining function position_of_AT()

def position_of_AT(dna):
  cou = 0
  y = 0
  for x in dna:
    y = y + 1
    if x == 'a':
    #  print (y)
      if (dna[y]) == 't':
        cou = y - 1
        print ('The position of AT is %s' % cou)
        break

# Calling function position_of_AT()
position_of_AT(dna)
