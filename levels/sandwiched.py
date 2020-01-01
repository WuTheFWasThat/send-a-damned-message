from utils import alphabet

def cut_sandwiched(x):
    pieces = [x]
    for letter in reversed(alphabet):
        new_pieces = []
        for piece in pieces:
            indices = [i for i, l in enumerate(piece) if l == letter]
            if len(indices) >= 2:
                first, last = indices[0], indices[-1]
                new_pieces.append(piece[:first])
                new_pieces.append(piece[last + 1:])
            else:
                new_pieces.append(piece)
        pieces = new_pieces
    return ''.join(pieces)
