import fire
import random
import readline

_COLORS = dict(
    green="\033[92m",
    blue="\033[94m",
    red="\033[91m",
    yellow="\033[93m",
)
_COLORS_END = "\033[0m"
def _colored(t, color):
    return _COLORS[color] + t + _COLORS_END

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
    """vowels bleed, x's stop it"""
    chars = [l for l in x]
    newchars = [l for l in chars]
    cancerous = 'aeiou'
    for vowel in cancerous:
        for i, l in enumerate(chars):
            if l.lower() == vowel:
                if i != 0 and newchars[i-1] != ' ' and newchars[i-1].lower() not in cancerous:
                    if newchars[i-1] == 'x':
                        newchars[i-1] = None
                    else:
                        newchars[i-1] = l
                if i != len(chars) - 1 and newchars[i+1] != ' ' and newchars[i+1].lower() not in cancerous:
                    if newchars[i+1] == 'x':
                        newchars[i+1] = None
                    else:
                        newchars[i+1] = l
    return ''.join([l for l in newchars if l is not None])

def quote_hell(x):
    """
    spaces reverse groups
    single quotes are literal quotes
    double quotes just group
    """
    i = 0
    def read_quote(quotechar=None):
        nonlocal i
        result = ''
        while i < len(x):
            l = x[i]
            i += 1
            if l == ' ' and quotechar is not "'":
                result2 = read_quote(quotechar)
                return result2 + ' ' + result
            if l == quotechar:
                return result
            if l == '"' and quotechar is None:
                result += read_quote('"')
            elif l == "'" and quotechar is None:
                result += read_quote("'")
            else:
                result += l
        return result
    return read_quote()

def _rotate_alphabet(x, direction):
    is_upper = x == x.upper()
    val = ord(x.lower()) - ord('a')
    newval = (val + direction) % 26
    new_x = chr(newval + ord('a'))
    if is_upper:
        new_x = new_x.upper()
    return new_x

def extend_sequences(x):
    prev = None
    direction = None
    result = []
    for char in x + ' ':
        cur = char
        if prev is not None:
            new_direction = None
            if direction is not None:
                target = _rotate_alphabet(prev, direction)
                if cur != target:
                    result.append(target)
                    new_direction = None
                else:
                    new_direction = direction
            if cur == _rotate_alphabet(prev, 1):
                new_direction = 1
            elif cur == _rotate_alphabet(prev, -1):
                new_direction = -1
            elif cur == prev:
                new_direction = 0
            if direction is None and new_direction is None:
                result.append(prev)
            direction = new_direction
        prev = cur
    return ''.join(result)


def switchbacks(x):
    """
    Paths reach for each other, also break if there are two switches
    """
    def reduce_path(path):
        segments = []
        cur_dir = 0
        segment = [path[0]]
        for char in path[1:]:
            new_dir = ord(char.lower()) - ord(segment[-1].lower())
            assert abs(new_dir) <= 1
            if abs(new_dir - cur_dir) == 2:
                segments.append(segment)
                segment = [segment[-1], char]
                cur_dir = new_dir
            else:
                segment.append(char)
                if cur_dir == 0:
                    cur_dir = new_dir
        segments.append(segment)
        for i in range(1, len(segments) - 1):
            segment = segments[i]
            new_segment = [segment[0]]
            prev = segment[0]
            for char in segment[1:]:
                if char == prev:
                    new_segment.append(char)
                prev = char
            new_segment.append(segment[-1])
            segments[i] = new_segment
        result = [*segments[0]]
        for segment in segments[1:]:
            assert segment[0] == result[-1], f'{segment[0]} != {result[-1]}'
            result.extend(segment[1:])
        return result

    result = []
    curpath = []
    for char in x:
        if char.lower() not in alphabet:
            if len(curpath):
                result.extend(reduce_path(curpath))
                curpath = []
            result.append(char)
        else:
            if len(curpath):
                diff = ord(char.lower()) - ord(curpath[-1].lower())
                if abs(diff) > 1:
                    sign = 1 if diff > 0 else -1
                    result.extend(reduce_path(curpath))
                    result.append(_rotate_alphabet(curpath[-1], sign))
                    if abs(diff) > 2:
                        result.append(_rotate_alphabet(char, -sign))
                    curpath = []
            curpath.append(char)
    if len(curpath):
        result.extend(reduce_path(curpath))
    return ''.join(result)

def count_words(x):
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

# def ordered_cyclic_permute_3(x):
#     n = len(x)
#     seed = sum([ord(l) for l in x])
#     my_rand = random.Random(seed)
#     indices = list(range(n))
#     my_rand.shuffle(indices)
#     chars = [l for l in x]
#     for i in range(0, n-2, 3):
#         ind_1, ind_2, ind_3 = indices[i:i+3]
#         chars[ind_1] = x[ind_2]
#         chars[ind_2] = x[ind_3]
#         chars[ind_3] = x[ind_1]
#     return ''.join(chars)

def ordered_cyclic_permute_3(x):
    n = len(x)
    n3 = (n // 3) * 3
    newchars = [l for l in x]
    for i in range(0, n3 // 3):
        ind_1 = i
        ind_2 = n3 // 3 + i
        ind_3 = 2 * n3 // 3 + i
        if i % 2 == 1:
            ind_2, ind_3 = ind_3, ind_2
        newchars[ind_1] = x[ind_2]
        newchars[ind_2] = x[ind_3]
        newchars[ind_3] = x[ind_1]
    return ''.join(newchars)


def lonely_death(x):
    """vowels/consonants are enemies.  those surrounded by enemies die.  y's are both"""
    chars = [l for l in x]
    types = []
    deaths = []
    for l in chars:
        if l.lower() in 'aeiou':
            t = 'v'
        elif l.lower() in 'bcdfghjklmnpqrstvwxz':
            t = 'c'
        elif l.lower() in 'y':
            t = 'vc'
        else:
            t = ' '
        types.append(t)
        deaths.append(False)
    for i in range(len(chars)):
        if types[i] == ' ':
            continue
        has_ally = False
        if i != 0 and types[i] in types[i-1]:
            has_ally = True
        if i != len(chars)-1 and types[i] in types[i+1]:
            has_ally = True
        if not has_ally:
            deaths[i] = True
    return ''.join([x for x, d in zip(chars, deaths) if not d])

# example='The quick brown fox jumped over the lazy dog'
levels = [
    dict(
        name='W',
        fn=switchbacks,
        goal='a damned message',
        # answer='a dcbabcdefghijklm',
        # answer="Send a daklpocdbc meqrutage"
    ),
    dict(
        name='Rot',
        fn=rot_word,
        goal='a damned message',
        answer='amnedd essagem a',
    ),
    # dict(
    #     name='Sub',
    #     fn=substitution,
    #     goal='a damned message',
    #     answer='t ztyjez yevvtxe',
    # ),
    dict(
        name='Un',
        fn=count_words,
        goal='Damn it',
        answer='DDDDammmmmmmmmmmmmnnnnnnnnnnnnnn iiiiiiiiitttttttttttttttttttt',
    ),
    dict(
        name='Step',
        fn=extend_sequences,
        goal='a damned message',
        answer="a daklngfd meqrutage"
    ),
    dict(
        name='Cancer',
        fn=cancerous_vowels,
        goal='a damned message',
        answer='a dxaxmnxexd mxexssxaxgxe',
    ),
    dict(
        name='Fold',
        fn=needs_palindromic_redundancy,
        goal='a damned message',
        answer='a damned messageegassem denmad a',
    ),
    dict(
        name='Lonely',
        fn=lonely_death,
        goal='a damned message',
        answer='ay dyamneyd myessaygey',
    ),
    dict(
        name='Tricky',
        fn=ordered_cyclic_permute_3,
        goal='a really really really really really really really really really stupidly damned long message',
        answer='la lt pedlyydrmael  oeglmysraaeayrsauli le laynrdalln  eelsygre leylryarla le leylryarla le l',
    ),
    dict(
        name='Quote',
        fn=quote_hell,
        goal='"She said, \'Send a damned message\'", he said',
        answer="""
        '"She said, '"message' damned a 'Send"'", he said'
        """.strip(),
    ),
    # accumulate sum within word?

    # something like lempel ziv?

    # something where it quickly blows up?
    # e.g. between each pair of letters, add their average?
    # maybe you have to solve system of equations to prevent blowup
]

def smart_input(x, color=None):
    if color is None:
        return input(x)
    y = input(x + _COLORS[color])
    print(_COLORS_END, end='')
    return y

def main(one_player=True, skip=0):
    for level in levels:
        if 'answer' in level:
            assert level['fn'](level['answer']) == level['goal'], f"'{level['fn'](level['answer'])}'"

    def clear_screen():
        if one_player:
            return
        # TODO: better
        for _ in range(1000):
            print()

    def yesno(msg):
        while True:
            w = smart_input(msg)
            if w.lower() in ['y', 'yes']:
                return True
            if w.lower() in ['n', 'no']:
                return False
            print("Unable to parse, please type 'y' or 'n'")

    i = skip
    while True:
        if i >= len(levels):
            print('Congrats!  Game over')
            return
        if i < 0:
            print('Already at level 1')
            i = 0

        level = levels[i]
        # print(f'Level {i+1}: {level["name"]}')
        print(f'Level {i+1}')
        while True:
            print('GOAL IS TO SEND:')
            print(_colored(level["goal"], 'green'))
            print()
            x = smart_input('Send your message:\n', color='yellow')
            if x == 'SKIP':
                i += 1
                break
            if x == 'BACK':
                i -= 1
                break
            y = level['fn'](x)
            if y == level['goal']:
                smart_input('Passed level!')
                clear_screen()
                i += 1
                break
            if not one_player:
                clear_screen()
                smart_input('Pass the laptop! Press enter when laptop has switched hands')
                clear_screen()
                print()
            # yesno('Decode?')
            print('Received damned message:')
            print(_colored(y, 'red'))
            print()

if __name__ == "__main__":
    fire.Fire(main)
