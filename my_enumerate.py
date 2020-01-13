


def my_enum(obj, start=0):
    c = start
    for i in obj:
        yield (c, i)
        c += 1


