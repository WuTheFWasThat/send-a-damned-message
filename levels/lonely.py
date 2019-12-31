def lonely_death(x):
    """vowels/consonants are enemies.  those surrounded by enemies die.  y's are both"""
    chars = [l for l in x]
    types = []
    for l in chars:
        if l.lower() in 'aeiou':
            t = 'v'
        elif l.lower() in 'bcdfghjklmnpqrstvwxz':
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
