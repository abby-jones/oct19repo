temperature = 33
if (temperature > 30):
    print('too hot \nargh')
elif (temperature < 0):
    print('too cold')
else:
    print('perfect')

# this is better than using several ifs because when using many ifs, the programme evaluates each statement
# and prints multiple outputs if more than one condition is met, which we don't want

# similarly, using if if else is not good because if the first statement is true, then the next one is false,
# the programme will print the output of the first if statement, as well as what follows the else part