def please(x):
    "Ternary operator, abc -> aabc"
    i = 0

    def read_expr():
        nonlocal i
        if i == len(x):
            return ''
        word = ''
        words = []

        while i < len(x):
            letter = x[i]
            i += 1
            if letter == ')':
                break

            if letter == '!':
                if i < len(x):
                    word += x[i]
                    i += 1
            elif letter == '(':
                word += read_expr()
            elif letter == ' ':
                words.append(word)
                word = ''
            else:
                word += letter
        words.append(word)

        # print('words', words)
        def parse_words(words):
            if len(words) < 3:
                return ' '.join(words)
            a, b = words[:2]
            c = parse_words(words[2:])
            return ' '.join([a, b, c, c])
        assert len(words) >= 1
        return parse_words(words)
    return read_expr()


assert please('') == ''
assert please('a') == 'a'
assert please('a b') == 'a b'
assert please('a b c') == 'a b c c'
assert please('a b c d e') == 'a b c d e e c d e e'
assert please(' a b') == ' a b b'
assert please('a b ') == 'a b  '
assert please('( a b) c') == ' a b b c'
assert please('(a b ) c') == 'a b   c'
assert please('a (b c)') == 'a b c'
assert please('a !(b c)') == 'a (b c c'
assert please('() a (() b c)') == ' a  b c c  b c c'
assert please('(a b) c d') == 'a b c d d'
assert please('a b c d') == 'a b c d c d'
assert please('a (b (c (d') == 'a b c d'
assert please('() !c !!d') == ' c !d !d'
