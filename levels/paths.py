from utils import rotate_alphabet, is_alphabet

def _reduce_path(path):
    if not len(path):
        return ''
    segments = []
    cur_dir = None
    last = None
    segment = []
    for cur in path:
        if last is not None:
            new_dir = ord(cur.lower()) - ord(last.lower())
            if abs(new_dir) > 1:  # jump
                sign = 1 if new_dir > 0 else -1
                segments.append((segment + [last], cur_dir or 0))
                segments.append(([rotate_alphabet(last, sign), rotate_alphabet(cur, -sign)], 'Jump'))
                segment = []
                new_dir = None
            elif cur_dir is None or new_dir == cur_dir:  # continue
                segment.append(last)
            elif new_dir == 0:  # sloped to flat
                segments.append((segment, cur_dir))
                segment = [last]
            elif cur_dir == 0:  # go from flat to sloped
                segments.append((segment + [last], cur_dir))
                segment = []
            else:  # V or ^ shape
                segments.append((segment, cur_dir))
                segments.append(([last], 0))
                segment = []
            cur_dir = new_dir
        last = cur
    assert last is not None
    segments.append((segment + [last], cur_dir or 0))

    result = []
    # print('segments', segments)
    for i, (segment, dir) in enumerate(segments):
        assert dir in [-1, 1, 0, 'Jump'], dir
        if dir == 0:
            if i > 0 and i < len(segments) - 1 and segments[i-1][1] == segments[i+1][1] and segments[i-1][1] != 'Jump':  # 1,0,1 or -1,0,-1 pattern
                segment = segment[1:]
        if dir in [-1, 1]:
            if (i == 0 or segments[i-1][1] != 'Jump') and (i == len(segments) - 1 or segments[i+1][1] != 'Jump'):  # chain breaks
                if i == 0:
                    result.append(segment[0])
                if i == len(segments) - 1:
                    result.append(segment[-1])
                segment = []
        result.extend(segment)
        # print('segment', segment, 'new result', result)
    # print('final result', result)
    return ''.join(result)

def paths(x):
    """Jumps in letters reach for each other, consecutive chains break."""
    result = ''
    curpath = []
    for char in x:
        if not is_alphabet(char):
            result += _reduce_path(curpath) + char
            curpath = []
        else:
            curpath.append(char)
    result += _reduce_path(curpath)
    return result

def test_reduce_path(s, expected):
    assert _reduce_path(s) == expected, f'{_reduce_path(s)} != {expected}'

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

if 0:
    all_ms = set()
    cur = 'a damned message'
    while True:
        print(cur)
        if cur in all_ms:
            break
        all_ms.add(cur)
        cur = paths(cur)
    print(len(all_ms))
