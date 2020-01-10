type state = {
  prev: option(char),
  count: int,
  result: string,
};

let fn = (x) => {
  /*
     vowels bleed, spaces stop it
   */
  let maybe_chars = Array.of_list(
    List.map((x) => Some(x), Utils.char_list(x))
  );

  ignore(List.mapi((i, char) => {
    switch (Utils.is_vowel(char)) {
      | false => ignore()
      | true => {
        ignore(List.map(
          (dir) => {
            if (Belt.Option.map(Utils.safe_get(x, i+dir), (x) => Utils.is_vowel(x)) == Some(false)) {
              Array.set(maybe_chars, i+dir, if (String.get(x, i+dir) == ' ') None else Some(char))
            }
          },
          [-1, 1]
        ))
      }
    }
  }, Utils.char_list(x)))

   maybe_chars |> Array.to_list |> Utils.filter_none |> Utils.join_char_list
}

let level: Types.level = {
  name: "cancer",
  fn: fn,
  goal: "a damned message",
  answer: "a  d a mn e d m e ss a g e ",
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a aba c"), "aaaac")
Utils.assert_eq(fn("a eba c"), "aeaac")
Utils.assert_eq(fn("ebcda c"), "eecaac")
Utils.assert_eq(fn("ys too"), "ys ooo")
