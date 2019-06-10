strings = ['kuraki', 'str', 'string']

for index, string in enumerate(strings):
    if 'str' in string:
        strings[index] = 'kuraki    '
print(strings)