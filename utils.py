alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rotate_alphabet(x, direction):
    is_upper = x == x.upper()
    val = ord(x.lower()) - ord('a')
    newval = (val + direction) % 26
    new_x = chr(newval + ord('a'))
    if is_upper:
        new_x = new_x.upper()
    return new_x
