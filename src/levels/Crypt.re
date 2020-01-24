let is_consonant = (x) => {
  (Char.lowercase_ascii(x) == 'y') || Utils.is_consonant(x)
}

let is_vowel = (x) => {
  (Char.lowercase_ascii(x) == 'y') || Utils.is_vowel(x)
}

let fn = (x) => {
  /* consonants die unless surrounded by two vowels.  y's are both
     */
  x |> Utils.map_words((s) => {
    let chars = Utils.char_list(s);
    chars |> List.mapi(
      (i, char) => {
        let prev = Utils.safe_get_list(chars, i-1) |> Utils.unwrap_or(' ');
        let next = Utils.safe_get_list(chars, i+1) |> Utils.unwrap_or(' ');
        let both_vowels = is_vowel(prev) && is_vowel(next);
        if (is_consonant(char)) {
          if (both_vowels) { Some(char) } else { None }
        } else {
          Some(char)
        }
      }
    ) |> Utils.filter_none |> Utils.join_char_list;
  })
}

let level: Types.level = {
  name: "crypt",
  fn: fn,
  goal: "a dayum message",
  answer: "a ydayumy ymesysage",
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
Utils.assert_eq(fn("ababa"), "ababa")
Utils.assert_eq(fn("aattyaattyaatt"), "aaaaaa")
Utils.assert_eq(fn("aya byb"), "aya ")
Utils.assert_eq(fn("ayyyb"), "ayy")

