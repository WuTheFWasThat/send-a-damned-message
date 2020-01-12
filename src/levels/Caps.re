let fn = (x) => {
  let n = String.length(x);
  Utils.char_list(x) |> List.mapi((i, l) => {
    let prev = Utils.safe_get(x, i-1);
    let next = Utils.safe_get(x, i+1);
    let l = if (i > 0 && Utils.is_alphabet(Utils.unwrap(prev)) && Utils.is_upper(Utils.unwrap(prev))) {
      Utils.swap_case(l)
    } else { l };
    let l = if (i < n-1 && Utils.is_alphabet(Utils.unwrap(next)) && Utils.is_upper(Utils.unwrap(next))) {
      Utils.swap_case(l)
    } else { l };
    l
  }) |> Utils.join_char_list;
}

let level: Types.level = {
  name: "caps",
  fn: fn,
  goal: "A DAMNED MESSAGE",
  answer: "A dAmnEd MesSagE",
}

Utils.assert_eq(fn("aB"), "AB")
Utils.assert_eq(fn("a B"), "a B")
Utils.assert_eq(fn("aBC"), "Abc")
Utils.assert_eq(fn("aBCd"), "AbcD")
Utils.assert_eq(fn("aBCde"), "AbcDe")
