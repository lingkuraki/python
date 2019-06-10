import fileinput


def process(string):
    print('processing:', string)


# 每次迭代一个字符
with open('E:\python\chapter11\something.txt') as f:
    while True:
        char = f.read(1)
        if not char:
            break
        process(char)

# 每次迭代一行
with open('..\something.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        process(line)

# 延迟迭代
for line in fileinput.input("..\somefile.txt"):
    process(line)
