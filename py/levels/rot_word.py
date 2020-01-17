def rot_word(x):
    def rotate(l):
        return l[-1:] + l[:-1]
    return '' if not x else ' '.join(rotate([rotate(w) for w in x.split(' ')]))

"""
def rot_word(x):
    n = len(x)
    if n <= 1:
        return x
    m = n // 2
    return x[m:] + rot_word(x[:m])
"""

def rot_word(x):
    n = len(x)
    i = 1
    while i < n:
        x = x[i:2*i] + x[:i] + x[2*i:]
        i *= 2
    return x

x = 'a damned message'
y = rot_word(x)
while y != x:
    print(y)
    y = rot_word(y)
