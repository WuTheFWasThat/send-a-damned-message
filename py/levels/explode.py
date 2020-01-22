def fn(x):
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


assert fn('a b') == 'a a b'
assert fn('a b c') == 'a a b c'
assert fn('a b c d e') == 'a a b c a a b c d e'
assert fn(' a b') == 'a b'
assert fn('" a b" c') == ' a b  a b c'
assert fn(' a ( b c)') == 'a b c'
assert fn('() a (() b c)') == 'a b c'
assert fn('(a b) c d') == 'a a b a a b c d'
assert fn('a b c d') == 'a a b c a a b c d'
assert fn('"(a b)" c d') == '(a b) (a b) c d'
assert fn('() "c" "d"') == 'c d'
assert fn(""" '"' "'" c """.strip()) == """ " " ' c """.strip()

level = dict(
    fn=fn,
    goal='(please) send a short "damned" message wouldn\'t you?',
    answer='() \'(please) send a short "damned" message\' "wouldn\'t you?"',
    # answer=""" ( please, ( just ( a ( short ( damned message"""
)
