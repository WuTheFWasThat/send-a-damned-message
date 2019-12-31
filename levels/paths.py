from utils import rotate_alphabet, alphabet

def _reduce_path(path):
    if not len(path):
        return []
    segments = []
    cur_dir = None
    last = None
    segment = []
    for char in path:
        if last is not None:
            new_dir = ord(char.lower()) - ord(last.lower())
            if abs(new_dir) > 1:
                segments.append((segment + [last], cur_dir or 0))
                sign = 1 if new_dir > 0 else -1
                segments.append(([
                    rotate_alphabet(last, sign),
                    rotate_alphabet(char, -sign)
                ], 'Jump'))
                segment = []
                new_dir = None
            elif cur_dir is not None and new_dir != cur_dir:
                if new_dir == 0:
                    segments.append((segment, cur_dir))
                    segment = [last]
                elif cur_dir == 0:
                    segments.append((segment + [last], cur_dir))
                    segment = []
                else:  # V or ^ shape
                    segments.append((segment, cur_dir))
                    segments.append(([last], 0))
                    segment = []
            else:
                segment.append(last)
            cur_dir = new_dir
        last = char
    assert last is not None
    segments.append((segment + [last], cur_dir or 0))

    result = []
    # print('segments', segments)
    for i, (segment, dir) in enumerate(segments):
        assert dir in [-1, 1, 0, 'Jump']
        if dir == 0:
            if i > 0 and i < len(segments) - 1 and segments[i-1][1] == segments[i+1][1] and segments[i-1][1] != 'Jump':
                segment = segment[1:]
        if dir in [-1, 1]:
            # print('i', i, segments)
            if i > 0 and segments[i-1][1] == 'Jump':
                pass
            elif i < len(segments) - 1 and segments[i+1][1] == 'Jump':
                pass
            else:
                if i == 0:
                    result.append(segment[0])
                if i == len(segments) - 1:
                    result.append(segment[-1])
                segment = []
        result.extend(segment)
        # print('segment', segment, 'new result', result)

    # print('result', result)
    return result

def paths(x):
    """Jumps in letters reach for each other, consecutive chains break."""
    result = []
    curpath = []
    for char in x:
        if char.lower() not in alphabet:
            result.extend(_reduce_path(curpath))
            curpath = []
            result.append(char)
        else:
            curpath.append(char)
    result.extend(_reduce_path(curpath))
    return ''.join(result)

"""
TODO: a terrible programmer wrote this whole file, there are probably bugs
"""

def test_reduce_path(s, expected):
    actual = ''.join(_reduce_path(list(s)))
    assert actual == expected, f'{actual} != {expected}'

test_reduce_path('', '')
test_reduce_path('m', 'm')
test_reduce_path('jklmz', 'jklmnyz')
test_reduce_path('ajklm', 'abijklm')
test_reduce_path('jklm', 'jm')
test_reduce_path('abjklmyz', 'abcijklmnxyz')
test_reduce_path('abjjyz', 'abcijjkxyz')

test_reduce_path('aabcdef', 'aaf')
test_reduce_path('aabcdeft', 'aabcdefgst')
test_reduce_path('taabcdef', 'tsbaaf')

test_reduce_path('tabcdeff', 'tsbabcdeff')
test_reduce_path('abcdeff', 'aff')
test_reduce_path('abcdefft', 'affgst')

test_reduce_path('abcba', 'aca')
test_reduce_path('abababa', 'abababa')

test_reduce_path('abbc', 'abc')
test_reduce_path('abcdeffedcbabccd', 'affacd')
test_reduce_path('tabcdeffedcbabccd', 'tsbabcdeffacd')
"""
if 1:
    all_ms = set()
    cur = 'a damned message'
    while True:
        print(cur)
        if cur in all_ms:
            break
        all_ms.add(cur)
        cur = switchbacks(cur)
"""
