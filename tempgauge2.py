temperature = -10
if (temperature > 30):
    print('too hot')
    print('argh')
if (temperature < 0):
    print('too cold')
else:
    print('perfect')

# if temp is 20, it will print 'perfect'
# if temp is 40, it will print 'too hot' and 'argh' and 'perfect'
# if temp is -10, it will print 'too cold'

# ex6: e.g. before, if temp was 40, then 'too hot',
# 'aagh' and 'perfect' would be printed
# but now it will only print the first 2 messages
# so 'perfect' is the output of values above 0, 
# up to and including 30

