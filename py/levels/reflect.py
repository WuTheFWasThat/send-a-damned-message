from utils import is_consonant

# def reflect(x):
#     for i, char in enumerate(x):
#         if is_consonant(char):
#             return reflect(x[i+1:][::-1]) + char + x[:i][::-1]
#     return x
#
#
# def almost_inv_reflect(x):
#     res = ''
#     for char in x:
#         if is_consonant(char):
#             res = ''.join(reversed(res))
#         res += char
#     res = ''.join(reversed(res))
#     return res


def milk(x):
    if not x: return x
    return x[0] + reflect(x[1:][::-1])

def reflect(x):
    if not x: return x
    return reflect(x[1:][::-1]) + x[0]

def inv_reflect(x):
    res = ''
    for char in x:
        res = ''.join(reversed(res))
        res += char
    res = ''.join(reversed(res))
    return res


if 0:
    def print_cycle(cur):
        all_ms = set()
        while True:
            print(cur)
            if cur in all_ms:
                break
            all_ms.add(cur)
            assert inv_reflect(reflect(cur)) == cur, f'{inv_reflect(cur)} != {cur}'
            cur = reflect(cur)
        print(len(all_ms))
    cur = 'yet another damned message'
    print_cycle(cur)

    # cycle of the "milk shuffle", see http://oeis.org/A003558
    # from utils import alphabet
    # for ll in range(26):
    #     print(ll, alphabet[:ll])
    #     print_cycle(alphabet[:ll])

level = dict(
    fn=reflect,
    goal="a damned message",
    answer="easmdna adme esg",
)
