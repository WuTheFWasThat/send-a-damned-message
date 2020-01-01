from utils import num2a

def count_words(x):
    prev = ''
    count = 0
    result = []
    for char in x + ' ':
        if char == prev:
            count += 1
        else:
            if count != 0:
                newchar = num2a(min(count, 26) - 1)
                if prev == prev.upper():
                    newchar = newchar.upper()
                result.append(newchar)
            prev = char
            count = 1
            if char == ' ':
                result.append(char)
                count = 0
                prev = ''
    return ''.join(result[:-1])

assert count_words('b AA  cc') == 'a B  b'

level = dict(
    name='Un',
    fn=count_words,
    goal='Damn it',
    answer='DDDDammmmmmmmmmmmmnnnnnnnnnnnnnn iiiiiiiiitttttttttttttttttttt',
)
