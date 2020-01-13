from utils import a2num, is_alphabet

def codebook(x):
    print('x', x)
    s = 'abcdefghijklmnopqrstuvwxyz '
    for word in x.split(' '):
        if not word:
            continue
        i = a2num(word[0], with_spaces=False)
        i = min(len(s) - 1, i)
        removed_letter = s[i]
        print('remove at ', i)
        s = s[:i] + s[i + 1:]
        for l in word[1:]:
            i = a2num(l, with_spaces=False)
            i = min(len(s) - 1, i)
            print('add at ', i)
            s = s[:i] + removed_letter + s[i:]
    print('return', s)
    return s

assert codebook("") == "abcdefghijklmnopqrstuvwxyz "
assert codebook("b") == "acdefghijklmnopqrstuvwxyz "
assert codebook("ba") == "bacdefghijklmnopqrstuvwxyz "
assert codebook("bb") == "abcdefghijklmnopqrstuvwxyz "
assert codebook("a a a a a ") == "fghijklmnopqrstuvwxyz "
