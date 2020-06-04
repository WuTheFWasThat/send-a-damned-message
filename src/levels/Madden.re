type state = {
  result: string,
  last: int,
  lastchar: char,
}

let fn = (x) => {
  let n = String.length(x);
  if (n == 0) {
    x
  } else {
    let s = Utils.range(n, ~start=1) |> List.fold_left(
      (state, i) => {
        let c = String.get(x, i);
        if (c == state.lastchar) {
          {
            result: state.result ++ (String.sub(x, state.last, i - state.last) |> Utils.reverse_str),
            last: i,
            lastchar: c
          }
        } else {
          {...state, lastchar: c}
        }
      },
      {
        result: "",
        last: 0,
        lastchar: String.get(x, 0),
      }
    );
    s.result ++ (String.sub(x, s.last, n - s.last) |> Utils.reverse_str)
  }
}

let level: Types.level = {
  name: "madden",
  old_names: [],
  fn: fn,
  goal: "a damned message demands a sage me",
  answer: "sem denmad aassdnamed eggas a  eem",
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "a")
Utils.assert_eq(fn("abab"), "baba")
Utils.assert_eq(fn("abba"), "baab")
Utils.assert_eq(fn("baab"), "abba")
Utils.assert_eq(fn("sand"), "dnas")
Utils.assert_eq(fn("sanadweeb"), "ewdanasbe")
Utils.assert_eq(fn("sanadweneb"), "benewdanas")
Utils.assert_eq(fn("abbasa nadweeb"), "baewdan asabbe")
