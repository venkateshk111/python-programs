# Python program to print n number of stars

n = int(input('Enter row value: '))
m = int(input('enter column value'))

for i in range(n) :
    for j in range(m):
        print('*', end=' ')
        if j==m :
            print("\n")
print() # this is for zsh shell to avoid printing %