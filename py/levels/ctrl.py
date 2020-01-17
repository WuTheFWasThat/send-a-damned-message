from utils import a2num, is_alphabet, rotate_alphabet

"""
def ctrl(x):
    print('x', x)
    s = 'abcdefghijklmnopqrstuvwxyz '
    for word in x.split(' '):
        if not word:
            continue
        i = a2num(word[0], with_spaces=False)
        i = min(len(s) - 1, i)
        removed_letter = s[i]
        s = s[:i] + s[i + 1:]
        for l in word[1:]:
            i = a2num(l, with_spaces=False)
            i = min(len(s) - 1, i)
            s = s[:i] + removed_letter + s[i:]
    return s

assert ctrl("") == "abcdefghijklmnopqrstuvwxyz "
assert ctrl("b") == "acdefghijklmnopqrstuvwxyz "
assert ctrl("ba") == "bacdefghijklmnopqrstuvwxyz "
assert ctrl("bb") == "abcdefghijklmnopqrstuvwxyz "
assert ctrl("a a a a a ") == "fghijklmnopqrstuvwxyz "
"""


"""
def ctrl(x):
    # print('x', x)
    s = ''
    for word in x.split(' '):
        if not len(word):
            continue
        l_to_add = word[0]
        for char in word[1:]:
            i = a2num(char, with_spaces=False)
            # print(x, i, len(s))
            if i > len(s):
                s = s + ' ' * (i - len(s)) + l_to_add
            else:
                s = s[:i] + l_to_add + s[i:]

        # print(s)
    return s

assert ctrl("") == ""
assert ctrl("b") == ""
assert ctrl("ba") == "b"
assert ctrl("bb") == " b"
assert ctrl("bc") == "  b"
assert ctrl("a a a  a a ") == ""
assert ctrl("abb bcc cdd a a ") == " abccba"
assert ctrl("za za ua ba za za ia fa") == "fizzbuzz"
assert ctrl("a damned message") == "md  mdmm d        dd mm"
#     goal='a damned message',
#     answer='ec gc ac scc ec mc db eb nb mb ab db aa',
"""

def ctrl(x):
    # print('x', x)
    s = ' '
    offset = 0
    i = 0
    for char in x:
        if char == ' ':
            offset = len(s)
            s = s + s
            i = 0
        else:
            ind = offset + (i % (len(s) - offset))
            new_l = rotate_alphabet(s[ind], a2num(char, with_spaces=True), with_spaces=True).lower()
            # i = a2num(char, with_spaces=False)
            # print(x, i, len(s))
            s = s[:ind] + new_l + s[ind+1:]
            i += 1

        # print(s)
    return s

assert ctrl("") == " "
assert ctrl("b") == "b"
assert ctrl("ba") == "c"
assert ctrl("bb") == "d"
assert ctrl("bc") == "e"
assert ctrl("a a a a a") == "abbbbbbbbbbbbbbb"
assert ctrl("abb bcc cdd a a ") == "emlqfmlqfmlqfmlqemlqfmlqfmlqfmlq"
assert ctrl("a damned message") == "aols"
print(ctrl("a z ca lnac zmarfnba"))
#     goal='a damned message',
#     answer='ec gc ac scc ec mc db eb nb mb ab db aa',
