a = int(input("Please enter a number: "))
b = int(input("Please enter a number: "))
c = int(input("Please enter a number: "))

if (a > b) and (a > c):
    print(a)
elif (a > b) and (a < c):
    print(c)
elif (a < b) and (b > c):
    print(b)
else: 
    print(c)

############################

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)