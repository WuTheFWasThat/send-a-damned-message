type state = {
  prev: option(char),
  count: int,
  result: string,
};

let fn = (x) => {
  let result = List.fold_left(
    (s: state, cur) => {
      switch (s.prev == Some(cur)) {
        | true => { result: s.result, prev: s.prev, count: s.count + 1 }
        | false => {
          let result = if (s.count > 0) {
            s.result ++ Char.escaped(Utils.cased_like(Utils.num2a(min(s.count, 26) - 1), Utils.unwrap(s.prev)))
          } else {
            s.result
          }

          if (cur == ' ') {
            { result: result ++ Char.escaped(' '), count: 0, prev: None }
          } else {
            { result: result, count: 1, prev: Some(cur) }
          }
        }
      }
    },
  { result: "", prev: None, count: 0 },
  List.concat([Utils.char_list(x), [' ']]),
  ).result;

  String.sub(result, 0, String.length(result) - 1)
}

let level: Types.level = {
  name: "unwary",
  fn: fn,
  goal: "Damn it",
  answer: "DDDDammmmmmmmmmmmmnnnnnnnnnnnnnn iiiiiiiiitttttttttttttttttttt",
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("b AA  cc"), "a B  b")
