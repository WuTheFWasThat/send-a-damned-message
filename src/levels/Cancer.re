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
        switch (i != 0 && !Utils.is_vowel(String.get(x, i-1))) {
          | true => Array.set(maybe_chars, i-1, (String.get(x, i-1) == ' ') ? None : Some(char));
          | false => ignore()
        }
        switch (i != String.length(x) - 1 && !Utils.is_vowel(String.get(x, i+1))) {
          | true => Array.set(maybe_chars, i+1, (String.get(x, i+1) == ' ') ? None : Some(char));
          | false => ignore()
        }
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
