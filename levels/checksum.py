from utils import a2num, is_alphabet

def checksum(x):
    words = x.split(' ')
    results = []
    for word in words:
        if len(word) == 0:
            results.append('')
        elif len(word) == 1:
            results.append('-')
        else:
            assert len(word) > 1
            orig = word[:-1]
            truesum = sum([
                a2num(l) + 1 for l in orig if is_alphabet(l)
            ]) % 26
            # print(truesum)
            if (a2num(word[-1]) + 1) % 26 == truesum:
                results.append(orig)
            else:
                results.append('-' * len(orig))
    return ' '.join(results)
