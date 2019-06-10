# 检查用户名和PIN码

database = [
    ['albert', '1234'],
    ['dilbert', '3256'],
    ['kuraki', '123456'],
    ['lingbo', '2332']
]

username = input("User name: ")
pin = input('PIN code: ')

if [username, pin] in database: print('Access granted')