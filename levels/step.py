from utils import rotate_alphabet

def extend_sequences(x):
    prev = None
    direction = None
    result = []
    for char in x + ' ':
        cur = char
        if prev is not None:
            new_direction = None
            if direction is not None:
                target = rotate_alphabet(prev, direction)
                if cur != target:
                    result.append(target)
                    new_direction = None
                else:
                    new_direction = direction
            if cur == rotate_alphabet(prev, 1):
                new_direction = 1
            elif cur == rotate_alphabet(prev, -1):
                new_direction = -1
            elif cur == prev:
                new_direction = 0
            if direction is None and new_direction is None:
                result.append(prev)
            direction = new_direction
        prev = cur
    return ''.join(result)
