def fn(x):
    n = len(x)
    starts = [0]
    ends = []
    for i in range(1, n):
        if x[i] == x[i - 1]:
            starts.append(i)
            ends.append(i)
    ends.append(n)
    xs = [
        x[s:e] for (s, e) in zip(starts, ends)
    ]
    return ''.join([
        part[::-1] for part in xs
    ])
