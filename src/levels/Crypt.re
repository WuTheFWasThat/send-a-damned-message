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
        let prev = Utils.safe_get_list(chars, i-1) |> Utils.unwrap_or('y');
        let next = Utils.safe_get_list(chars, i+1) |> Utils.unwrap_or('y');
        let both_vowels = is_vowel(prev) && is_vowel(next);
        let both_consonants = is_consonant(prev) && is_consonant(next);
        if (is_vowel(char) && is_consonant(char)) {
          if (both_consonants || both_vowels) { Some(char) } else { None }
        } else if (is_vowel(char)) {
          if (both_consonants) { Some(char) } else { None }
        } else if (is_consonant(char)) {
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
  answer: "a dayum mesyaasage",
}

// a dayum message
// a dyayuym myeyssyaygye
Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("aa bb"), " ")
Utils.assert_eq(fn("abab"), "abab")
Utils.assert_eq(fn("ay yb"), "ay yb")
Utils.assert_eq(fn("a yy b"), "a yy b")
Utils.assert_eq(fn("a yyy b"), "a yyy b")
Utils.assert_eq(fn("aabb"), "")
Utils.assert_eq(fn("abbab"), "aab")
Utils.assert_eq(fn("ababa"), "ababa")
Utils.assert_eq(fn("aattyaattyaatt"), "")
Utils.assert_eq(fn("aya byb"), "aya byb")
Utils.assert_eq(fn("ayyyb"), "ayyyb")

