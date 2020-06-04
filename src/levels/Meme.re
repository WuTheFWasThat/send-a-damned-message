let fn = (x) => {
  let chars = Utils.char_list(x) |> List.map((x) => Some(x)) |> Array.of_list;
  let bigrams = Js.Dict.empty();
  List.map(
    (i) => {
      let bigram = String.sub(x, i, 2);
      Js.Dict.set(
        bigrams, bigram,
        (Js.Dict.get(bigrams, bigram) |> Utils.unwrap_or(0)) + 1,
      );
    },
    Utils.range(String.length(x) - 1),
  ) |> ignore;

  List.map(
    (i) => {
      let bigram = String.sub(x, i, 2);
      if (Js.Dict.get(bigrams, bigram) |> Utils.unwrap_or(0) > 1) {
        Array.set(chars, i, None);
        Array.set(chars, i+1, None);
      } |> ignore;
    },
    Utils.range(String.length(x) - 1),
  ) |> ignore;

  chars |> Array.to_list |> Utils.filter_none |> Utils.join_char_list;
}

let level: Types.level = {
  name: "meme", // "dang", "murmur", "george"
  old_names: [],
  // magma, onion, sense, verve
  fn: fn,
  goal: "a danged message",
  answer: "a danged messagzzze",
}

Utils.assert_eq(fn("aa bb"), "aa bb")
Utils.assert_eq(fn("a a "), "")
Utils.assert_eq(fn("abc zab ybc"), " z y")
