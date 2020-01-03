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
    vals = [None for _ in range(len(x))]

    def get_val(i):
        if vals[i] is not None:
            return vals[i]
        if i == 0:
            val = 0
        else:
            pow2 = 1
            while i % (pow2 * 2) == 0:
                pow2 *= 2
            val = (a2num(x[i - pow2], with_spaces=True) + get_val(i - pow2)) % 27
        vals[i] = val
        return val
    return ''.join(rotate_alphabet(l, get_val(i), with_spaces=True) for i, l in enumerate(x))


if 1:
    def print_cycle(cur):
        all_ms = set()
        while True:
            print(cur)
            if cur in all_ms:
                break
            all_ms.add(cur)
            cur = tournament(cur)
        print(len(all_ms))
    # interesting that this cycles, there some funny thing going on with capitalization too
    cur = 'a damned message'
    print_cycle(cur)
