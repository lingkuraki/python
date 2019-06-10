# 一个使用get()的简单数据库

# 将人名用作键的字段，每个人都用一个字典表示
people = {
    'Alice': {
        'phone': '1234',
        'addr': 'Foo driver 23'
    },
    'kuraki': {
        'phone': '0837',
        'addr': '潍坊 502'
    },
    'Ben': {
        'phone': '3586',
        'addr': 'Bar street 23'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name: ')

# 要查找电话号码还是地址
request = input('Phone number (p) or address (a)? ')

# 使用正确的键
key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# 使用get提供默认值
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print("{}'s {} is {}.".format(name, label, result))
