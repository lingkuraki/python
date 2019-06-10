def flatten(nested):
    try:
        # 不迭代类似于字符串的对象
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for subList in nested:
            for element in flatten(subList):
                yield element
    except TypeError:
        yield nested


a = list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))
print(a)
b = list(flatten(['foo', ['bar', ['kuraki']]]))
print(b)
