# Python program to find biggest of 3 numbers

a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number : '))

if a>b and a>c:
    print('%s is biggest number' %a)
elif b>c:
    print('%s is biggest number' %b)
else:
    print('%s is biggest number' %c)