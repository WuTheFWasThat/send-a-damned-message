def chain_define(x):
    words = []
    word = ''
    for char in x:
        if char == ' ' and word.strip():
            words.append(word)
            word = ''
        else:
            word += char
    words.append(word)

    if len(words) % 2 == 0:
        return ''

    defs = []
    def apply_defs(s):
        # print('applying defs', s, defs)
        for (k, v) in defs:
            assert len(k)
            s = v.join(s.split(k))
            # s = s.replace(k, v)
        return s

    i = 0
    while i < len(words) - 1:
        key = words[i]
        i += 1
        val = apply_defs(words[i])
        i += 1
        defs.append((key, val))

    assert i == len(words) - 1
    return apply_defs(words[i])


assert chain_define('') == ''
assert chain_define('b a c b c') == 'a'
assert chain_define('b  a c b c') == ' a'
assert chain_define('b a c b cab') == 'aaa'
assert chain_define('b c c b cab') == 'cac'
assert chain_define('b  a c  b abc') == 'a a  a'
assert chain_define(' b  a c  b abc') == 'ab a'
assert chain_define(' b  a b') == 'b'
assert chain_define('a b c') == 'c'
assert chain_define('a b c ') == ''
assert chain_define('a  ') == ''
assert chain_define('a b') == ''
assert chain_define('a b ') == ''
assert chain_define('a b  ') == ' '
assert chain_define('a fat fat b a') == 'b'
