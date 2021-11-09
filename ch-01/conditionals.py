# if, elif, else
print('Enter your age')
age = input()
age = int(age)
if (age < 18):
    print('you are a baby')
elif (age > 18 and age < 21):
    print('you still cant have beer')
else:
    print('i know that which you seek')

# while, break
i = 1;
while i <= 10:
    print(i)
    i += 1
    if (i == 6):
        break

j = 10
while j > 0:              
    j = j -1
    if j == 5:
        continue

    print(j)

# exe 1: fince lcm of x and y
x = 24
y = 36
lcm = y

while (True):
    if (lcm % x == 0 and lcm % y ==0):
        break
    lcm += 1 

print('LCM is', lcm)

# exe 2: Calculating Perfect Squares
print('Enter a number to see if it\'s a perfect square.')
val = abs(int(input()))
i = -1
square = False

while i <= val**0.5:
    i += 1
    if (i*i == val):
        square = True
        break

if (square):
    print(val, 'is a perfect square with square root of', i)
else:
    print('uh...just use a calculator')


# for
for i in 'hommie':
    print(i)

for i in range(1,10):
    print(i)

print("Good bye!")
