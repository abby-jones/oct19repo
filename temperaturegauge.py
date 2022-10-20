temperature = 40
if (temperature > 30):
    print('Too hot')
    print('Arghhhh')
    if (temperature > 50):
        print('AHHHHHH')
print('Too cold')

# if temp = 40 then 'too hot' and 'arghh'
# will be printed, and also 'too cold'

# if temp = 60 then all the statements will
# be printed

# if temp = 20 then nothing will be printed

# problems:
# if temp is less than 30 then nothing gets printed
# if temp is really hot, i.e. higher than 50,
# all the statements are printed which doesn't make sense
# need to use elifs and appropriately indent the code

temperature = 20
if (temperature > 30):
    print('too hot')
    print('argh')
if (temperature < 0):
    print('too cold')
if (temperature > 0):
    print('perfect')

# if temp is 20, it will print 'perfect'
