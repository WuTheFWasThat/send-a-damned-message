# everything except y!
consonants = 'bcdfghjklmnpqrstvwxz'
vowels = 'aeiou'

# def enemies(x):
#     """
#     vowels/consonants are enemies.  those next to enemies die.
#     y's are nobody's enemies but die when surrounded by two enemies
#     """
#     def are_enemies(a, b):
#         if a.lower() in vowels:
#             return b.lower() in consonants
#         elif a.lower() in consonants:
#             return b.lower() in vowels
#         return False
#
#     chars = [l for l in x]
#     deaths = [False for l in chars]
#     for i in range(len(chars)):
#         if i != 0 and are_enemies(chars[i], chars[i - 1]):
#             deaths[i] = True
#             deaths[i - 1] = True
#         if i > 1 and are_enemies(chars[i], chars[i - 2]) and chars[i-1] == 'y':
#             deaths[i - 1] = True
#     return ''.join([x for x, d in zip(chars, deaths) if not d])
#
# assert enemies('a damned message') == 'a  '
# assert enemies('a damnbed message') == 'a n '
# assert enemies('a daaamnbed message') == 'a an '


def lonely_death(x):
    """vowels/consonants are enemies.  those surrounded by enemies die.  y's are both"""
    chars = [l for l in x]
    types = []
    for l in chars:
        if l.lower() in vowels:
            t = 'v'
        elif l.lower() in consonants:
            t = 'c'
        elif l.lower() in 'y':
            t = 'vc'
        else:
            t = ''
        types.append(t)
    deaths = [False for l in chars]
    for i in range(len(chars)):
        has_ally = False
        if i != 0 and types[i] in types[i - 1]:
            has_ally = True
        if i != len(chars) - 1 and types[i] in types[i + 1]:
            has_ally = True
        if not has_ally:
            deaths[i] = True
    return ''.join([x for x, d in zip(chars, deaths) if not d])
