word = input('enter a word or enter exit to quit:  ')
x = len(word)

def func(word,x):
  if word == 'exit':
    quit()
  while x > 0:
    print(word[x-1], end="")
    x = x - 1 
func(word,x)

print ('')
