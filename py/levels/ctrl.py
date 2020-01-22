from utils import a2num, is_alphabet, rotate_alphabet

"""
def fn(x):
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

assert fn("") == "abcdefghijklmnopqrstuvwxyz "
assert fn("b") == "acdefghijklmnopqrstuvwxyz "
assert fn("ba") == "bacdefghijklmnopqrstuvwxyz "
assert fn("bb") == "abcdefghijklmnopqrstuvwxyz "
assert fn("a a a a a ") == "fghijklmnopqrstuvwxyz "
"""


"""
def fn(x):
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

assert fn("") == ""
assert fn("b") == ""
assert fn("ba") == "b"
assert fn("bb") == " b"
assert fn("bc") == "  b"
assert fn("a a a  a a ") == ""
assert fn("abb bcc cdd a a ") == " abccba"
assert fn("za za ua ba za za ia fa") == "fizzbuzz"
assert fn("a damned message") == "md  mdmm d        dd mm"
#     goal='a damned message',
#     answer='ec gc ac scc ec mc db eb nb mb ab db aa',
"""

def fn(x):
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

assert fn("") == " "
assert fn("b") == "b"
assert fn("ba") == "c"
assert fn("bb") == "d"
assert fn("bc") == "e"
assert fn("a a a a a") == "abbbbbbbbbbbbbbb"
assert fn("abb bcc cdd a a ") == "emlqfmlqfmlqfmlqemlqfmlqfmlqfmlq"
assert fn("a damned message") == "aols"
print(fn("a z ca lnac zmarfnba"))

level = dict(
    name='ctrl',
    fn=fn,
    goal='a damned message',
    answer='ec gc ac scc ec mc db eb nb mb ab db aa',
)
