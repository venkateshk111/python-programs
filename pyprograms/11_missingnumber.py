list = eval(input('enter the list: '))

for i, num in enumerate(list):
   if i+1 != num :
    print(i+1)
    break