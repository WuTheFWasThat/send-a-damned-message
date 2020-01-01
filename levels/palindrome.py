def needs_palindromic_redundancy(x):
    n = len(x)
    recovered = []
    for i in range(n // 2):
        if x[i] == x[n-i-1]:
            recovered.append(x[i])
        else:
            break
    return ''.join(recovered)

level = dict(
    name='Lap',  # fold?
    fn=needs_palindromic_redundancy,
    goal='a damned message',
    answer='a damned messageegassem denmad a',
)
