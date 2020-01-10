def chain_define(x):
    words = x.split(' ')
    # NOTE: without this section, this puzzle is impossible, i think
    while len(words) and words[-1] == '':
        words.pop()
    while '' in words:
        # i = words.index('')
        # use last index to avoid merging two ''
        i = len(words) - words[::-1].index('') - 1
        assert i != len(words) - 1
        assert words[i + 1] != ''
        words[i + 1] = ' ' + words[i + 1]
        words = words[:i] + words[i+1:]
    # end section
    print(words)

    i = 0
    defs = []
    def apply_defs(s):
        # print('applying defs', s, defs)
        for (k, v) in defs:
            assert len(k)
            s = v.join(s.split(k))
            # s = s.replace(k, v)
        return s

    while i < len(words) - 1:
        key = words[i]
        i += 1
        val = apply_defs(words[i])
        i += 1
        defs.append((key, val))

    if i < len(words):
        assert i == len(words) - 1
        return apply_defs(words[i])
    return ''


assert chain_define('') == ''
assert chain_define('b a c b c') == 'a'
assert chain_define('b  a c b c') == ' a'
assert chain_define('b a c b cab') == 'aaa'
assert chain_define('b c c b cab') == 'cac'
assert chain_define('b  a c  b abc') == 'a a  a'
assert chain_define(' b  a c  b abc') == 'ab a'
assert chain_define(' b  a b') == 'b'
assert chain_define('a b') == ''
assert chain_define('a b  ') == ''
