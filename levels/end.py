def end(x):
    if 's' not in x:
        return ''
    x1, x2 = x.split('s', 1)
    return x2 + x1
