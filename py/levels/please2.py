def please(x):
    "Ternary operator, a b c -> ab ac"

    def eval_words(words):
        if not len(words):
            return ''
        i = 1
        res = words[0]
        while i < len(words):
            a = res
            b = words[i]
            if i + 1 < len(words):
                c = words[i + 1]
                res = f'{a}{b} {a}{c}'
                i += 2
            else:
                res = f'{a}{b} {a}'
                i += 1
        return res

    def split_arr(arr, el):
        start = 0
        res = []
        i = start
        while i < len(arr):
            if arr[i] == el:
                res.append(arr[start:i])
                start = i+1
            i += 1
        res.append(arr[start:])
        return res

    def parse(words, n_dolls):
        if n_dolls == 0:
            return eval_words(words)
        words = [parse(w, n_dolls - 1) for w in split_arr(words, '$' * n_dolls)]
        return eval_words(words)

    words = x.split(' ')
    n_dolls = max([len(w) for w in words if w == '$' * len(w)] + [0])
    return parse(words, n_dolls)

assert please('') == ''
assert please('a') == 'a'
assert please(' a') == 'a '
assert please('a b') == 'ab a'
assert please('a b c') == 'ab ac'
assert please('a b c d') == 'ab acd ab ac'
assert please('a b c d e') == 'ab acd ab ace'
assert please(' a b') == 'a b'
assert please('a b ') == 'ab a'

level = dict(
    fn=please,
    goal='pretty pretty please just send a short damned message and maybe some money',
    answer='$$$$ $$$ $$ $ pretty $ pretty $$ $ please $ just $$$ $$ $ send $ a $$ $ short $ damned $$$$ $$$ $ message $ and $$$ $$ $ maybe $ some $$ money',
    # answer=""" ( please, ( just ( a ( short ( damned message"""
)
print("GOAL", please(level['goal']))
print(f"ATTEMPT '{please(level['answer'])}'")
assert please(level['answer']) == level['goal']
