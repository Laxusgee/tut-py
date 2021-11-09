"""
this is a doc string
"""
import keyword

# operations
print("1 + 2 = ", 1+2)
print("int(6.7) =", int(6.7))
print(float(5))
print(2**2, 5//4)
print((3 + 4j) - (2 +1j))

# variables
x = 5
y = 21
print(x+y, type(x))
y = y + 3.2
print(type(y))
x += 1
print(x)

# exe 1
x = 14
x += 1
x = (x/5)**2
print(x)

# keywords
print(keyword.kwlist)

# exe 2
a = 2
b = 3
c = 4
z = (a**2 + b**2 + c**2)**0.5
print("z = ", z)

# strings
x = 'i\'m a single quote'
y = "i'm a double quote"
z ='''
ulti-line strings take on the same syntax as a docstring.
The difference is that a docstring appears at the beginning of a document,
and a multi-line string is defined within the program.
'''
print(x,y,z)
print(x +' and '+ y)
print('yari '*3)
print(x, 'and', y)
print(len(z))
print(y[-10:])

owner = 'Lawrence Ferlinghetti'
age = 100
print('The founder of City Lights Bookstore, {}, is now {} years old.'.format(owner, age))

# Booleans
x = True
y = False
print(not x)

# user input
print('what is your name?')
name = input()
print('wow!', name, 'is such a  cool name')