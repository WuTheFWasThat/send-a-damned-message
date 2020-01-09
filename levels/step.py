from utils import rotate_alphabet, is_alphabet

def extend_sequences(x):
    prev = None
    direction = None
    result = []
    for char in x + ' ':
        cur = char
        if prev is not None:
            if direction is not None:
                target = rotate_alphabet(prev, direction)
                if cur != target:
                    result.append(target)

            new_direction = None
            for possible_dir in [1, 0, -1]:
                if cur == rotate_alphabet(prev, possible_dir):
                    new_direction = possible_dir
            if direction is None and new_direction is None:
                result.append(prev)
            direction = new_direction
        prev = cur if is_alphabet(cur) or cur == ' ' else None
    return ''.join(result)
