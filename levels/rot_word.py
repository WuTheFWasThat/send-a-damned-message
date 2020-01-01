def fn(x):
    rotate = lambda l: l[-1:] + l[:-1]
    return '' if not x else ' '.join(rotate([rotate(w) for w in x.split(' ')]))


level = dict(
    name='Rot',
    fn=fn,
    goal='a damned message',
    answer='amnedd essagem a',
)
