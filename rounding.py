# predicted output:
#int_num will be the interger version of number1
#float_num is float version of number2
#round_num will round the float number first,
# and then convert it to an integer to remove the .0
# then the integer number, float mumber, and rounded number will be printed

num1 = input('Enter whole number:')
num2 = input('Enter decimal number:')

int_num = int(num1)
float_num = float(num2)
round_num = int(round(float_num))

print(int_num, float_num, round_num)