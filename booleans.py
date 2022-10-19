num1 = float(input('Enter first number'))
num2 = float(input('Enter second number'))

if num1 > num2:
    num1bigger = True
else:
    num1bigger = False

print('It is ', num1bigger, 'that num1 is bigger')

# if the first number the user enters is bigger than the second 
# number then the variable num1bigger will be set to true
# otherwise it will be set to false