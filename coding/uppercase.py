x = input('Enter a word:  ')

def upper_case(x):
  for y in x:
    num = ord(y)
    if num > 96 and num < 123:
      num = num - 32
      letter = chr(num)
      x = x.replace(y, letter)
  print (x)

upper_case(x)
