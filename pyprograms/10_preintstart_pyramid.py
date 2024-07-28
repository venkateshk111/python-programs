# Python program to print n number of * as pyramid

n = int(input('Enter value for n: '))

for i in range(n):
   print((' '*(n-i-1))+ ('* ')*(i+1)) # normal pyramid


# # Inverted pyramid
# for i in range(n):
#     print(((' ')*i)+'* '*(n-i)) # Inverted pyramid

# ### for both pyramid or diamond

# for i in range(n):
#     print((' '*(n-i-1))+ ('* ')*(i+1)) # normal pyramid

# for i in range(n):
#     print(((' ')*i)+'* '*(n-i)) # Inverted pyramid