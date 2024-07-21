# Program to print sum of given numbers via cmd

from sys import argv

args = argv[1:]

sum = 0
for x in args:
    sum = sum + int(x)

print('The Sum of Given Numbers is = ',sum)
