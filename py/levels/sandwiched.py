from utils import alphabet

def reverse_sandwiched(x):
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

assert reverse_sandwiched('abba') == 'abba'
assert reverse_sandwiched('baab') == 'baab'
assert reverse_sandwiched('abab') == 'abab'
assert reverse_sandwiched('sand') == 'sand'
assert reverse_sandwiched('sanadweeb') == 'sanadweeb'
assert reverse_sandwiched('sanadweneb') == 'sanenadweb'
assert reverse_sandwiched('sanadnweeb') == 'sandanweeb'
assert reverse_sandwiched('sanmadnweeb') == 'samndanweeb'
assert reverse_sandwiched('bsanmadnweeb') == 'beewnmandasb'
assert reverse_sandwiched('bsanmadnweebanb') == 'beewnmanasbndab'
assert reverse_sandwiched('eeabea') == 'eebaea'

if 0:
    def print_cycle(cur):
        all_ms = set()
        while True:
            print(cur)
            if cur in all_ms:
                break
            all_ms.add(cur)
            cur = reverse_sandwiched(cur)
        print(len(all_ms))
    cur = 'a damned message'
    print_cycle(cur)

# OLD VERSION
# def cut_sandwiched(x):
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
