from utils import alphabet

def substitution(x):
    code = 'xpyhekovbntufilwqzcarsjgmd'
    def replace(l):
        if l in alphabet:
            return code[alphabet.index(l)]
        if l in alphabet.upper():
            return code.upper()[alphabet.upper().index(l)]
        return l
    return ''.join([replace(l) for l in x])

level = dict(
    fn=substitution,
    goal='a damned message',
    answer='t ztyjez yevvtxe',
)
