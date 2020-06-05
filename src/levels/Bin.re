// for 2^n size input, gives n size output
// each position is XOR of places where nth bit is 1

let rec binary = (n) => {
  if (n == 0) {
    []
  } else if (n mod 2 == 0) {
    List.concat([[0], binary(n / 2)])
  } else {
    List.concat([[1], binary((n-1) / 2)])
  }
}

let rec sum_lists = (a, b) => {
  if (List.length(a) == 0) {
    b
  } else if (List.length(b) == 0) {
    a
  } else {
    List.concat([
      [List.hd(a) + List.hd(b)],
      sum_lists(List.tl(a), List.tl(b))
    ])
  }
}

let fn = (x) => {
  /*
    Corruption by adding amount to a single position of each word
    Amount/position both determined by sum of letters
    Everything is mod 27 instead of 26 to make things work out better
  */
  let to_sum: list(list(int)) = Utils.char_list(x) |> List.mapi(
    (i, c) => {
      let bits: list(int) = binary(i+1);
      let amt: int = Utils.char2num(c);
      let amts: list(int) = bits |> List.map((b) => (b * amt));
      "amts" |> Js.log;
      amts |> Js.log;
      amts
    }
  );

  let sum = List.fold_left(sum_lists, [], to_sum);
  sum |> List.map((x) => {
    Utils.num2a(x mod 27, ~with_spaces=true)
  }) |> Utils.join_char_list
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "a")
Utils.assert_eq(fn("!"), " ")
Utils.assert_eq(fn("b"), "b")
Utils.assert_eq(fn("!"), " ")
Utils.assert_eq(fn("ab"), "ab")
Utils.assert_eq(fn("abc"), "de")
Utils.assert_eq(fn("aaaa"), "bba")
Utils.assert_eq(fn("aaaaaaaaaaaaaaa"), "hhhh")
Utils.assert_eq(fn("aaaaaaaaabaaaaa"), "hihi")
Utils.assert_eq(fn("aaaaaaaaaaaaaaaa"), "hhhha")

let level: Types.level = {
  name: "bin", //
  old_names: [],
  fn: fn,
  goal: "damn",
  answer: "da m   n",
}
