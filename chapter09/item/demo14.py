def CreateCounter():
    a = 0

    def counter():
        nonlocal a  # 使用外层变量
        a += 1
        return a

    return counter


counterA = CreateCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
