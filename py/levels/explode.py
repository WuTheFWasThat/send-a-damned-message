def explode(x):
    "Ternary operator, abc -> aabc"
    i = 0

    def read_expr(quote=None):
        nonlocal i
        if i == len(x):
            return ''
        word = ''

        if quote is not None:
            while i < len(x):
                letter = x[i]
                i += 1
                if letter == quote:
                    break
                else:
                    word += letter
            return word

        words = []

        while i < len(x):
            letter = x[i]
            i += 1
            if letter == ')':
                break

            if letter in ['"', "'"]:
                word += read_expr(letter)
            elif letter == '(':
                word += read_expr()
            elif letter == ' ':
                words.append(word)
                word = ''
            else:
                word += letter
        words.append(word)
        # print('words', words)
        while len(words) > 1:
            if len(words) == 2:
                words.append('')
            a, b, c = words[:3]
            new_word = ' '.join([x for x in [a, a, b, c] if len(x)])
            words = [new_word] + words[3:]
        assert len(words) == 1
        return words[0]
    return read_expr()


assert explode('a b') == 'a a b'
assert explode('a b c') == 'a a b c'
assert explode('a b c d e') == 'a a b c a a b c d e'
assert explode(' a b') == 'a b'
assert explode('" a b" c') == ' a b  a b c'
assert explode(' a ( b c)') == 'a b c'
assert explode('() a (() b c)') == 'a b c'
assert explode('(a b) c d') == 'a a b a a b c d'
assert explode('a b c d') == 'a a b c a a b c d'
assert explode('"(a b)" c d') == '(a b) (a b) c d'
assert explode('() "c" "d"') == 'c d'
assert explode(""" '"' "'" c """.strip()) == """ " " ' c """.strip()
