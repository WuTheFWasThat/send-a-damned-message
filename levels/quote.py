def quote_hell(x):
    "Ternary flip operator, abc -> bca.  Quotes group"
    i = 0

    def read_expr():
        nonlocal i
        if i == len(x):
            return ''
        letter = x[i]
        i += 1
        if letter != '"':
            return letter
        result = ''
        while i < len(x):
            letter = x[i]
            i += 1
            if letter != '"':
                result += letter
            else:
                break
        return result

    result = read_expr()
    while i < len(x):
        b = x[i]
        i += 1
        c = read_expr()
        result = b + c + result
    return result

# assert quote_hell('abcde') == 'bdaec'
# assert quote_hell('abcdef') == 'acebfd'
# assert quote_hell('ab"cd"ef') == 'FecdBa'
# assert quote_hell('a"bc"def') == 'DEFcb"a'
