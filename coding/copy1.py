x = input('Enter the file you want to copy:  ')

test = open(x)
y = (test.read())
print ('the copy of the file is:  %s' % x)

test_file = open('new_'+x, 'w')
test_file.write(y)

