type segment = list(char);
type direction = Continue(int) | Jump;
type _segment_and_dir = {
  segment: segment,
  direction: direction
}
type segments_state = {
  segments: list(_segment_and_dir),
  cur_dir: option(int),
  last: option(char),
  segment: segment,
}

let segment_str = (segment: _segment_and_dir) => {
  (segment.segment |> Utils.join_char_list) ++ " " ++ {
    switch (segment.direction) {
      | Continue(x) => { string_of_int(x) }
      | Jump => "jump"
    }
  }
}

let reduce_path = (x) => {
  if (String.length(x) == 0) {
    x
  } else {
    let res = List.fold_left(
      (s, cur) => {
        if (s.last == None) {
          {...s, last: Some(cur)}
        } else {
          let last = Utils.unwrap(s.last);
          let new_dir = Utils.a2num(cur) - Utils.a2num(last);
          if (abs(new_dir) > 1) {
            // CASE 1: jump
            let sign = (new_dir > 0) ? 1 : -1;
            let new_segments = [
              {
                segment: List.append(s.segment, [last]),
                direction: Continue(s.cur_dir |> Utils.unwrap_or(0))
              },
              {
                segment: [Utils.rotate_alphabet(last, sign), Utils.rotate_alphabet(cur, -sign)],
                direction: Jump,
              }
            ];
            {
              segments: List.append(s.segments, new_segments), segment: [],
              cur_dir: None, last: Some(cur),
            }
          } else if (s.cur_dir == None || s.cur_dir == Some(new_dir)) {
            // CASE 2: continue
            {
              segments: s.segments, segment: List.append(s.segment, [last]),
              cur_dir: Some(new_dir), last: Some(cur),
            }
          } else if (new_dir == 0) {
            // CASE 3: sloped to flat
            let new_segment = { segment: s.segment, direction: Continue(Utils.unwrap(s.cur_dir)) };
            {
              segments: List.append(s.segments, [new_segment]), segment: [last],
              cur_dir: Some(new_dir), last: Some(cur),
            }
          } else if (s.cur_dir == Some(0)) {
            // CASE 4: flat to sloped
            let new_segment = { segment: List.append(s.segment, [last]), direction: Continue(Utils.unwrap(s.cur_dir)) };
            {
              segments: List.append(s.segments, [new_segment]), segment: [],
              cur_dir: Some(new_dir), last: Some(cur),
            }
          } else {
            // CASE 5: V or ^ shape
            let new_segment1 = { segment: s.segment, direction: Continue(Utils.unwrap(s.cur_dir))};
            let new_segment2 = { segment: [last], direction: Continue(0)};
            {
              segments: List.append(s.segments, [new_segment1, new_segment2]), segment: [],
              cur_dir: Some(new_dir), last: Some(cur),
            }
            /*
            {
              segments: s.segments, segment: s.segment,
              cur_dir: Some(new_dir), last: Some(cur),
            }
            */
          }
        }
      },
      { segments: [], cur_dir: None, last: None, segment: [] },
      Utils.char_list(x),
    );

    let segments = Array.of_list(List.append(res.segments, [{
        segment: List.append(res.segment, [Utils.unwrap(res.last)]),
        direction: Continue(res.cur_dir |> Utils.unwrap_or(0))
    }]))

    let nsegments = Array.length(segments);

    // // Js.log(segments |> Js.Json.stringifyAny)
    // for (i in 0 to nsegments - 1) {
    //   let segment = segments[i];
    //   "Segment " ++ string_of_int(i) ++ ": " ++ segment_str(segment)  |> Js.log;
    // }

    let result = List.fold_left(
      (result, i) => {
        let {segment: segment, direction: dir} = segments[i];
        // segment |> Utils.join_char_list |> Js.log;
        let prev = Utils.safe_get_array(segments, i-1);
        let next = Utils.safe_get_array(segments, i+1);
        // 1,0,1 or -1,0,-1 pattern
        let is_saddle = (
          dir == Continue(0) && prev != None && next != None &&
          (Utils.unwrap(prev).direction == Utils.unwrap(next).direction) &&
          Utils.unwrap(prev).direction != Jump
        );
        let (segment, result) = if (is_saddle) {
          (List.tl(segment), result)
        } else if (dir == Continue(-1) || dir == Continue(1)) {
          if ((i == 0 || Array.get(segments, i-1).direction != Jump) &&
              (i == nsegments - 1 || Array.get(segments, i+1).direction != Jump)) {
            let first = (i == 0) ? [List.hd(segment)] : [];
            let last = (i == nsegments - 1) ? [List.nth(segment, List.length(segment) - 1)] : [];
            ([], List.concat([result, first, last]))
          } else {
            (segment, result)
          }
        } else {
          (segment, result)
        }

        // Js.log(
        //   "segment: " ++ (segment |> Utils.join_char_list) ++ " result " ++ (result |> Utils.join_char_list)
        // );
        List.append(result, segment)
        },
        [],
        Utils.range(Array.length(segments)),
    );
    let ret = result |> Utils.join_char_list
    // Js.log("final result: " ++ ret)
    ret
  }
}


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

let fn = (x) => { Utils.map_words(reduce_path, x) }

let level: Types.level = {
  name: "hike",
  fn: fn,
  goal: "a damned message",
  answer: "a dcbabcdefghijklmmnmlkjihgfeed mlkjihgfefghijklmnopqrssrqponmlkjihgfedcbabcdefgfe"
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("aeez blah "), reduce_path("aeez") ++ " " ++ reduce_path("blah") ++ " ")
Utils.assert_eq(fn("  test"), "  " ++ reduce_path("test"))
Utils.assert_eq(fn("simple"), reduce_path("simple"))
