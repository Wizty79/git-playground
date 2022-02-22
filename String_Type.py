x = 'seven'
print('x is {1:<9}  {0:>9} '.format(23, 56))
print(type(x))

#or use an f string instead, getting the same result

a = 23
b = 56
x = f'seven {a} {b}'
print('x is {}'. format(x))
print (type(x))


