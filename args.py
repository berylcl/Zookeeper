def myfunc(*args):
    out = []
    for num in args:
        if num % 2 == 0:
            out.append(num)
    return out
