x = int(input('Enter the smaller number: '))
y = int(input('Enter the larger number: '))

print('\n')

for i in range(x, y, 2):
    print(i)

print('\n')

Z = 0

while Z != (x + y):
    Z = x + y

print("Sum of the two numbers is: %d" % Z)
