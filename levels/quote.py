def quote_hell(x):
    "Ternary flip operator, abc -> CbA.  Quotes group"
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
        z = x[i]
        i += 1
        b = read_expr().swapcase()
        result = b + z + result.swapcase()
    return result

assert quote_hell('abcde') == 'EdcBa'
assert quote_hell('abcdef') == 'feDCbA'
assert quote_hell('ab"cd"ef') == 'FecdBa'
assert quote_hell('a"bc"def') == 'DEFcb"a'
