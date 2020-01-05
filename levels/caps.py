from utils import alphabet

def caps(x):
    result = list(x)
    for i, l in enumerate(x):
        if l in alphabet.upper():
            if i > 0:
                result[i-1] = result[i-1].swapcase()
            if i < len(x)-1:
                result[i+1] = result[i+1].swapcase()
    return ''.join(result)

assert caps('aB') == 'AB'
assert caps('aBC') == 'Abc'
assert caps('aBCd') == 'AbcD'
assert caps('aBCde') == 'AbcDe'
