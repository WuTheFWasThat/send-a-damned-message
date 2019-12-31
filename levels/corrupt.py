from utils import alphabet

def num(l):
    if l.lower() not in alphabet:
        return 0
    return (ord(l.lower()) - ord('a') + 1) % 27

def corrupt(x):
    if len(x) < 2:
        return x
    last = num(x[-1])
    x = x[:-1]
    index = (last-1) % len(x)
    new_num = (num(x[index]) + last-1) % 26
    new = chr(new_num + ord('a'))
    return x[:index] + new + x[index+1:]
