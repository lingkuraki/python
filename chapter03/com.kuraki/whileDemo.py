name = ''
while not name or name.isspace():
    name = input('Please enter your name: ')
print('Hello, {}!'.format(name))

for number in range(1, 101):
    print(number)
