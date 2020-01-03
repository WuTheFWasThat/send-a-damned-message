from utils import alphabet

def cut_sandwiched(x):
    n = len(x)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j]:
                pairs.append((i, j))

    is_outer = [False for _ in pairs]
    for pi, (i1, j1) in enumerate(pairs):
        # make sure no endpoint is contained within i1
        for (i2, j2) in pairs:
            if (i2 > i1 and i2 < j1) and (j2 > i1 and j2 < j1):
                is_outer[pi] = True
                break

    deleted = [False for _ in range(n)]
    for v, (i, j) in zip(is_outer, pairs):
        if not v:
            for k in range(i, j+1):
                deleted[k] = True
    return ''.join([l for k, l in enumerate(x) if not deleted[k]])

assert cut_sandwiched('abba') == 'aa'
assert cut_sandwiched('baab') == 'bb'
assert cut_sandwiched('abab') == ''
assert cut_sandwiched('sand') == 'sand'
assert cut_sandwiched('sanadweeb') == 'sdwb'
assert cut_sandwiched('sanadweneb') == 'sb'
assert cut_sandwiched('sanadnweeb') == 'swb'

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
