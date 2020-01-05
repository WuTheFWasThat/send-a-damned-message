def cancerous_vowels(x):
    """vowels bleed, periods stop it"""
    chars = [l for l in x]
    newchars = [l for l in chars]
    cancerous = 'aeiou'
    for vowel in cancerous:
        for i, l in enumerate(chars):
            if l.lower() == vowel:
                if i != 0 and chars[i-1].lower() not in cancerous:
                    if chars[i-1] == ' ':
                        newchars[i-1] = None
                    else:
                        newchars[i-1] = l
                if i != len(chars) - 1 and chars[i+1].lower() not in cancerous:
                    if chars[i+1] == ' ':
                        newchars[i+1] = None
                    else:
                        newchars[i+1] = l
    return ''.join([l for l in newchars if l is not None])

assert cancerous_vowels('a aba c') == 'aaaac'
assert cancerous_vowels('a eba c') == 'aeeac'
assert cancerous_vowels('ebcda c') == 'eecaac'
