x = input('what is your name:  ')
y = input('what is your favourite color:  ')

test_file = open('test_file.txt','a')

test_file.write(x)
test_file.write('\n')
test_file.write(y)
test_file.write('\n')

#with open("test_file.txt", "a") as f:
 #  f.write("new text")
