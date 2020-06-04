
let rec fn = (x) => {
  let n = String.length(x);
  switch (n == 0) {
    | true => x
    | false => {
      fn((String.sub(x, 1, n-1) |> Utils.reverse_str)) ++ String.sub(x, 0, 1)
    }
  }
}

let inv_fn = (x) => {
  let res = List.fold_left(
    (res, char) => {
        (res |> Utils.reverse_str) ++ String.make(1, char)
    },
    "", Utils.char_list(x)
  );
  res |> Utils.reverse_str
}

let level: Types.level = {
  name: "milk",
  old_names: [],
  fn: fn,
  goal: "a damned message",
  answer: "easmdna adme esg",
}

let verify_pair = (x, y) => {
  Utils.assert_eq(fn(x), y)
  Utils.assert_eq(inv_fn(y), x)
}

verify_pair("", "")
verify_pair("a", "a")
verify_pair("ab", "ba")
verify_pair("abc", "bca")
verify_pair("ab'c", "'bca")
verify_pair("abc'", "cb'a")
verify_pair("abcdefghijk lmnopqrstuv", " lkmjniohpgqfresdtcubva")
verify_pair("abcdefghijkl mnopqrstuvw", " lmknjoiphqgrfsetducvbwa")
