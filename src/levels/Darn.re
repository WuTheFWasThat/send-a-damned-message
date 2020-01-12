let fn = (x) => {
  /*
    Corruption by adding amount to a single position of each word
    Amount/position both determined by sum of letters
    Everything is mod 27 instead of 26 to make things work out better
  */
  let n = String.length(x)
  if (n == 0) {
      x
  } else {
    let total = Utils.char_list(x) |> List.map(
      l => Utils.a2num(l, ~with_spaces=true)
    ) |> Utils.sum;
    let index = (total + (n / 3)) mod n;
    let rotate = total + (n / 8)
    let new_char = Utils.rotate_alphabet(String.get(x, index), rotate, ~with_spaces=true);
    String.sub(x, 0, index) ++ Char.escaped(new_char) ++ String.sub(x, index + 1, n - index - 1)
  }
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "b")
Utils.assert_eq(fn("b"), "d")
Utils.assert_eq(fn("a damned message"), "a darned message")

let level: Types.level = {
  name: "darn",
  fn: fn,
  goal: "a damned message",
  answer: "a damned messagp",
}


