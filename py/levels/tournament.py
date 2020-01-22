# lol, this just shifts
# def tournament(x):
#     def play_tournament(y, inds):
#         if not inds:
#             return y
#         next_inds = []
#         for i in range(0, len(inds)-1, 2):
#             j1, j2 = inds[i], inds[i + 1]
#             y[j1], y[j2] = y[j2], y[j1]
#             next_inds.append(j1)
#         return play_tournament(y, next_inds)
#
#     return ''.join(play_tournament(list(x), range(len(x))))

from utils import rotate_alphabet, a2num

def tournament(x):
    vals = [0 for _ in range(len(x))]

    def parent(i):
        if i == 0:
            return None
        else:
            pow2 = 1
            while i % (pow2 * 2) == 0:
                pow2 *= 2
            return i - pow2

    for i, l in enumerate(x):
        j = parent(i)
        while j is not None:
            vals[j] += a2num(l, with_spaces=True)
            j = parent(j)
    return ''.join(rotate_alphabet(l, vals[i], with_spaces=True) for i, l in enumerate(x))

level = dict(
    name='Tree',
    fn=tournament,
    goal='a damned message',
    answer='k caunadqmmskabe',
)
