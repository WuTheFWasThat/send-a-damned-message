
type segment = list(char)
type segments_state = {
  segments: list((segment, int)),
  cur_dir: option(int),
  last: option(char),
  segment: segment,
}

let reduce_path = (x) => {
  let res = List.fold_left(
    (s, cur) => {
      s
    },
  { segments: [], cur_dir: None, last: None, segment: [] },
  List.concat([Utils.char_list(x), [' ']]),
  );
  // |> Utils.join_char_list
  x
}

/*
def _reduce_path(path):
    if not len(path):
        return ''
    for cur in path:
        if last is not None:
            new_dir = ord(cur.lower()) - ord(last.lower())
            if abs(new_dir) > 1:  # jump
                sign = 1 if new_dir > 0 else -1
                segments.append((segment + [last], cur_dir or 0))
                segments.append(([Utils.rotate_alphabet(last, sign), Utils.rotate_alphabet(cur, -sign)], 'Jump'))
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

*/

/*
Utils.assert_eq(reduce_path(""), "")
Utils.assert_eq(reduce_path("m"), "m")
Utils.assert_eq(reduce_path("jklmz"), "jklmnyz")
Utils.assert_eq(reduce_path("ajklm"), "abijklm")
Utils.assert_eq(reduce_path("jklm"), "jm")
Utils.assert_eq(reduce_path("abjklmyz"), "abcijklmnxyz")
Utils.assert_eq(reduce_path("abjjyz"), "abcijjkxyz")

Utils.assert_eq(reduce_path("aabcdef"), "aaf")
Utils.assert_eq(reduce_path("aabcdeft"), "aabcdefgst")
Utils.assert_eq(reduce_path("taabcdef"), "tsbaaf")

Utils.assert_eq(reduce_path("tabcdeff"), "tsbabcdeff")
Utils.assert_eq(reduce_path("abcdeff"), "aff")
Utils.assert_eq(reduce_path("abcdefft"), "affgst")

Utils.assert_eq(reduce_path("abcba"), "aca")
Utils.assert_eq(reduce_path("abababa"), "abababa")

Utils.assert_eq(reduce_path("abbc"), "abc")
Utils.assert_eq(reduce_path("abcdeffedcbabccd"), "affacd")
Utils.assert_eq(reduce_path("tabcdeffedcbabccd"), "tsbabcdeffacd")
*/

type state = {
  word: string,
  result: string,
};
let fn = (x) => { Utils.map_words(reduce_path, x) }

let level: Types.level = {
  name: "hike",
  fn: fn,
  goal: "a damned message",
  // answer: "a dcbabcdefghijklmmnmlkjihgfeed mlkjihgfefghijklmnopqrssrqponmlkjihgfedcbabcdefgfe"
  answer: "a damned message"
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("aeez blah "), reduce_path("aeez") ++ " " ++ reduce_path("blah") ++ " ")
Utils.assert_eq(fn("  test"), "  " ++ reduce_path("test"))
Utils.assert_eq(fn("simple"), reduce_path("simple"))
