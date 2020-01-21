let is_consonant = (x) => {
  (Char.lowercase_ascii(x) == 'y') || Utils.is_consonant(x)
}

let is_vowel = (x) => {
  (Char.lowercase_ascii(x) == 'y') || Utils.is_vowel(x)
}

let fn = (x) => {
  /* consonants die unless surrounded by two vowels.  y's are both
     */
  let chars = Utils.char_list(x);
  chars |> List.mapi(
    (i, char) => {
      let prev = Utils.safe_get_list(chars, i-1) |> Utils.unwrap_or(' ');
      let next = Utils.safe_get_list(chars, i+1) |> Utils.unwrap_or(' ');
      if (is_consonant(char)) {
        if (is_vowel(prev) && is_vowel(next)) {
          Some(char)
        } else {
          None
        }
      } else {
        Some(char)
      }
    }
  ) |> Utils.filter_none |> Utils.join_char_list;
}

let level: Types.level = {
  name: "crypt",
  fn: fn,
  goal: "a damned message",
  answer: "a ydyamyneydy ymyesysaygye",
}

// a dayum message
// a dyayuym myeyssyaygye
Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("aa bb"), "aa ")
Utils.assert_eq(fn("abab"), "aba")
Utils.assert_eq(fn("ay yb"), "a ")
Utils.assert_eq(fn("a yy b"), "a  ")
Utils.assert_eq(fn("a yyy b"), "a y ")
Utils.assert_eq(fn("aabb"), "aa")
Utils.assert_eq(fn("abbab"), "aa")

