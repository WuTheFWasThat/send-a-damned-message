let saves = (x, y) => {
  /* returns whether x saves y */
  if (Char.lowercase_ascii(x) == 'y') {
    true
  } else if (Char.lowercase_ascii(y) == 'y') {
    false
  } else if (Utils.is_vowel(x)) {
    Utils.is_vowel(y)
  } else if (Utils.is_consonant(x)) {
    Utils.is_consonant(y)
  } else {
    false
  }
}

let fn = (x) => {
  /* vowels/consonants are enemies.  those surrounded by enemies die.  y's are both
     */
  let chars = Utils.char_list(x);
  chars |> List.mapi(
    (i, char) => {
      let prev = Utils.safe_get_list(chars, i-1) |> Utils.unwrap_or(' ');
      let next = Utils.safe_get_list(chars, i+1) |> Utils.unwrap_or(' ');
      if (!(Utils.is_vowel(char) || Utils.is_consonant(char))) {
        Some(char)
      } else if (saves(prev, char) || saves(next, char)) {
        Some(char)
      } else {
        None
      }
    }
  ) |> Utils.filter_none |> Utils.join_char_list;
}

let level: Types.level = {
  name: "crypt",
  fn: fn,
  goal: "a damned message",
  answer: "ay dyamneyd myessaygey",
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("aa bb"), "aa bb")
Utils.assert_eq(fn("ay yb"), "a b")
Utils.assert_eq(fn("a yy b"), " yy ")
Utils.assert_eq(fn("aabb"), "aabb")
Utils.assert_eq(fn("abab"), "")

