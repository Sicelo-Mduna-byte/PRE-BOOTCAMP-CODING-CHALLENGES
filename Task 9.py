Multiples_of_three = []
Multiples_of_five = []



for i in range(3, 1000, 3):
    Multiples_of_three.append(i)
x = (sum(Multiples_of_three))
    
for i in range(5, 1000, 5):
    '''
    range(5, 1000) will give the sequence of numbers from 5 to 999 eg(5,6,6  ....999)
    range(5,1000,5) display every fifth number starting from five eg( 5, 10, 15 ....)
    '''
    Multiples_of_five.append(i)
y = (sum(Multiples_of_five))
'''
sum() is a built in standard function, that return the sum of a list
'''

print("The sum of all the multiples of 3 and 5 below 16 is: %d " % (x + y))