name = input('enter a full name:  ')

def full_name(name):
  space = 0
  count = 0
  for x in name:
    num = ord(x)
    count = count + 1
    if num > 96 and num < 123 and count == 1:
      num = num - 32
    if space == 1:
      num = num - 32
    print (chr(num), end="")
    if x == ' ':
      space = 1

full_name(name)


print ('')
