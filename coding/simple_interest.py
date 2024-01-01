amount = input('What is the starting amount:  ')
interest = input('What is the interest:  ')
time = input('What is the number of years:  ')
amount = int(amount)
interest = int(interest)
time = int(time)

def simple_interest(amount, interest, time):
    interest = (amount * interest * time)/100
    print ('=============================================================')
    print ('Simple interest gained:  %s' % interest)
    final = interest + amount
    print ('Total:  %s' % final)
    print ('=============================================================')

simple_interest(amount, interest, time)

def compound_interest(amount, interest, time):
    final = amount * (1 + (interest/100))**time
    compound = final - amount
    print ('=============================================================')
    print ('Compound interest gained:  %s' % compound)
    print ('Total:  %s' % final)
    print ('=============================================================')

compound_interest(amount, interest, time)    
