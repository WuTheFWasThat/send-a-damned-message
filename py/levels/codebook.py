from utils import a2num, is_alphabet

def codebook(x):
    if ' ' not in x:
        return ''
    book, code = x.split(' ', 1)
    return ''.join([
        book[a2num(l) % len(book)] if is_alphabet(l) else l
        for l in code
    ])
