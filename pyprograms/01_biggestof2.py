# Python program to find biggest of 2 numbers

x = int(input('Enter First num: '))
y = int(input('Enter Second num: '))

if x > y :
    print('Number %s is bigger num' %x)
elif x < y:
    print('Number %s is bigger num' %y)
else :
    print ('Both numbers %s and %s are Equal' %(x,y))