def lines(file):
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():  # 去掉两端的空格符
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
