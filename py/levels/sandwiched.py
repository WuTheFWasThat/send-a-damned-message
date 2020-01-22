from utils import alphabet

def fn(x):
    n = len(x)
    i = 0
    while i < n:
        for j in range(i + 1, n):
            if x[i] == x[j]:
                x = x[:i] + x[i:j + 1][::-1] + x[j + 1:]
                # NOTE: this makes it way easier i = j
                break
        i += 1
    return x

assert fn('abba') == 'abba'
assert fn('baab') == 'baab'
assert fn('abab') == 'abab'
assert fn('sand') == 'sand'
assert fn('sanadweeb') == 'sanadweeb'
assert fn('sanadweneb') == 'sanenadweb'
assert fn('sanadnweeb') == 'sandanweeb'
assert fn('sanmadnweeb') == 'samndanweeb'
assert fn('bsanmadnweeb') == 'beewnmandasb'
assert fn('bsanmadnweebanb') == 'beewnmanasbndab'
assert fn('eeabea') == 'eebaea'

if 0:
    def print_cycle(cur):
        all_ms = set()
        while True:
            print(cur)
            if cur in all_ms:
                break
            all_ms.add(cur)
            cur = fn(cur)
        print(len(all_ms))
    cur = 'a damned message'
    print_cycle(cur)

# OLD VERSION
# def fn(x):
#    pieces = [x]
#     for letter in reversed(alphabet):
#         new_pieces = []
#         for piece in pieces:
#             indices = [i for i, l in enumerate(piece) if l == letter]
#             if len(indices) >= 2:
#                 first, last = indices[0], indices[-1]
#                 new_pieces.append(piece[:first])
#                 new_pieces.append(piece[last + 1:])
#             else:
#                 new_pieces.append(piece)
#         pieces = new_pieces
#     return ''.join(pieces)


"""
key: swaps happen in order of output messgae
a damees
working backwards

a damned message
ssage --> want this before swapping S, gives "ssage"
egasse --> want this before swapping E, gives "essage"
em1'egasse --> want this before swapping E, gives "e1message"
menm1'egasse --> want this before swapping M, gives "mne1message"
age1mnemasse --> want this before swapping A, gives "amne1message"
degad mnemasse --> want this before swapping D, gives "damned message"
 daged mnemasse --> want this before swapping space, gives "damned message"
ad aged mnemasse --> want this before swapping space, gives "damned message"
"""

level = dict(
    fn=fn,
    goal='a damned message',
    answer='ad aged mnemasse',
)
