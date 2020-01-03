def chain_define(x):
    words = x.split(' ')
    i = 0
    defs = []
    def apply_defs(s):
        print('applying defs', s, defs)
        for (k, v) in reversed(defs):
            if not k:
                s = v.join(list(s))
            else:
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
