def cancerous_vowels(x):
    """vowels bleed, x's stop it"""
    chars = [l for l in x]
    newchars = [l for l in chars]
    cancerous = 'aeiou'
    for vowel in cancerous:
        for i, l in enumerate(chars):
            if l.lower() == vowel:
                if i != 0 and newchars[i-1] != ' ' and chars[i-1].lower() not in cancerous:
                    if newchars[i-1] == 'x':
                        newchars[i-1] = None
                    else:
                        newchars[i-1] = l
                if i != len(chars) - 1 and newchars[i+1] != ' ' and chars[i+1].lower() not in cancerous:
                    if newchars[i+1] == 'x':
                        newchars[i+1] = None
                    else:
                        newchars[i+1] = l
    return ''.join([l for l in newchars if l is not None])

