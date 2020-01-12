let fn = (x) => {

  let n = String.length(x);
  Utils.range((n + 1) / 2) |> List.fold_left((s, i) => {
    if (String.get(x, i) == String.get(x, n - 1 - i)) {
      s ++ Char.escaped(String.get(x, i))
    } else {
      s
    }
  }, "");
}

let level: Types.level = {
  name: "mum",
  fn: fn,
  goal: "a damned message",
  answer: "a damned messageegassem denmad a",
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "a")
Utils.assert_eq(fn("abracadabra"), "aaa")
Utils.assert_eq(fn("aaa"), "aa")
Utils.assert_eq(fn("abacadacaba"), "abacad")
Utils.assert_eq(fn("abacadacabra"), "a")
Utils.assert_eq(fn("some with space"), "t")
Utils.assert_eq(fn("some with spac"), " ")
Utils.assert_eq(fn("a damned message"), "")
