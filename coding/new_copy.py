test = open('fox.txt')
x = (test.read())
print (x)

test_file = open('new_fox.txt', 'w')
test_file.write(x)
