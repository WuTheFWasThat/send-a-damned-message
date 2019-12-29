import fire
import random

def rot_word(x):
    def rotate(l):
        return l[-1:] + l[:-1]
    return '' if not x else ' '.join(rotate([rotate(w) for w in x.split(' ')]))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def substitution(x):
    code = 'xpyhekovbntufilwqzcarsjgmd'
    def replace(l):
        if l in alphabet:
            return code[alphabet.index(l)]
        if l in alphabet.upper():
            return code.upper()[alphabet.upper().index(l)]
        return l
    return ''.join([replace(l) for l in x])

def cancerous_vowels(x):
    """vowels bleed, x's escape"""
    chars = [l for l in x]
    escaped = []
    i = 0
    while i < len(chars):
        if chars[i] == 'x':
            chars = chars[:i] + chars[i+1:]
            if i < len(chars):
                escaped.append(True)
        else:
            escaped.append(False)
        i += 1

    assert len(chars) == len(escaped)
    newchars = [l for l in chars]
    cancerous = 'aeiou'
    for vowel in cancerous:
        for i, (l, e) in enumerate(zip(chars, escaped)):
            if l.lower() == vowel and not e:
                if i != 0 and newchars[i-1] != ' ' and newchars[i-1].lower() not in cancerous:
                    newchars[i-1] = l
                if i != len(chars) - 1 and newchars[i+1] != ' ' and newchars[i-1].lower() not in cancerous:
                    newchars[i+1] = l
    return ''.join(newchars)

def count_words(x):
    i = 0

    prev = ''
    count = 0
    result = []
    for char in x + ' ':
        if char == prev:
            count += 1
        else:
            if count != 0:
                newchar = alphabet[min(count-1, 26)]
                if prev == prev.upper():
                    newchar = newchar.upper()
                result.append(newchar)
            prev = char
            count = 1
            if char == ' ':
                result.append(char)
                count = 0
    return ''.join(result[:-1])

def needs_palindromic_redundancy(x):
    n = len(x)
    recovered = []
    for i in range(n // 2):
        if x[i] == x[n-i-1]:
            recovered.append(x[i])
        else:
            break
    return ''.join(recovered)

def random_permute_3cycle(x):
    n = len(x)
    seed = sum([ord(l) for l in x])
    my_rand = random.Random(seed)
    indices = list(range(n))
    my_rand.shuffle(indices)
    chars = [l for l in x]
    for i in range(0, n-2, 3):
        ind_1, ind_2, ind_3 = indices[i:i+3]
        chars[ind_1] = x[ind_2]
        chars[ind_2] = x[ind_3]
        chars[ind_3] = x[ind_1]
    return ''.join(chars)

# example='The quick brown fox jumped over the lazy dog'
levels = [
    dict(
        fn=rot_word,
        goal='Send a damned message',
        answer='a amnedd essagem endS',
    ),
    dict(
        fn=substitution,
        goal='Send a damned message',
        answer='Vejz t ztyjez yevvtxe',
    ),
    dict(
        fn=count_words,
        goal='Damn it',
        answer='DDDDammmmmmmmmmmmmnnnnnnnnnnnnnn iiiiiiiiitttttttttttttttttttt',
    ),
    dict(
        fn=needs_palindromic_redundancy,
        goal='Send a damned message',
        answer='Send a damned messageegassem denmad a dneS',
    ),
    dict(
        fn=cancerous_vowels,
        goal='Send a damned message',
        answer='Sxend xa dxamnxed mxessxagxe',
    ),
    dict(
        fn=random_permute_3cycle,
        goal='Send a damned message',
        answer='eda aee mdSgam ndessn',
    ),
]

def main(one_player=True, skip=0):
    for level in levels:
        assert level['fn'](level['answer']) == level['goal'], level['fn'](level['answer'])

    def clear_screen():
        if one_player:
            return
        # TODO: better
        for _ in range(1000):
            print()

    def yesno(msg):
        while True:
            w = input(msg)
            if w.lower() in ['y', 'yes']:
                return True
            if w.lower() in ['n', 'no']:
                return False
            print("Unable to parse, please type 'y' or 'n'")

    for i, level in list(enumerate(levels))[skip:]:
        print(f'Level {i+1}')
        while True:
            print(f'GOAL: "{level["goal"]}"')
            print()
            x = input('Send your damned message:\n')
            y = level['fn'](x)
            if y == level['goal']:
                input('Passed level!  You may inform your partner.')
                clear_screen()
                break
            if not one_player:
                clear_screen()
                input('Pass the laptop! Press enter when laptop has switched hands')
                clear_screen()
                print()
            # yesno('Decode?')
            print('Received damned message:')
            print(y)
            print()

if __name__ == "__main__":
    fire.Fire(main)
