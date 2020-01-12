type state = {
  word: string,
  words: list(string),
  index: int,
};

let fn = (x) => {
  /*
    Ternary operator, abc -> aabc
  */
  let n = String.length(x);
  let rec read_words = (s: state): state => {
    if (s.index == n) { s } else {
      let letter = String.get(x, s.index);
      if (letter == ')') {
        { ...s, index: s.index + 1 }
      } else if (letter == ' ') {
        read_words({ word: "", words: List.append(s.words, [s.word]), index: s.index + 1 });
      } else if (letter == '!') {
        if (s.index + 1 == n) {
          read_words({ word: s.word, words: s.words, index: s.index + 1 })
        } else {
          let new_letter = Char.escaped(String.get(x, s.index + 1));
          read_words({ word: s.word ++ new_letter, words: s.words, index: s.index + 2 })
        }
      } else if (letter == '(') {
        let new_s = read_words({ words: [], word: "", index: s.index + 1 });
        let result = process_words(List.append(new_s.words, [new_s.word]) |> Array.of_list);
        read_words({ words: s.words, word: s.word ++ result, index: new_s.index })
      } else {
        read_words({ word: s.word ++ Char.escaped(letter), words: s.words, index: s.index + 1 })
      }
    }
  } and process_words = (words: array(string)): string => {
    let nw = Array.length(words);
    if (nw < 3) {
      words |> Js.Array.joinWith(" ")
    } else {
      // a b c -> a a b (c)
      let repeated = process_words(Array.sub(words, 2, nw-2));
      Array.append(Array.sub(words, 0, 2), Array.of_list([repeated, repeated]), ) |> Js.Array.joinWith(" ");
    }
  }

  let s = read_words({word: "", words: [], index: 0});
  process_words(List.append(s.words, [s.word]) |> Array.of_list)
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "a")
Utils.assert_eq(fn("a b"), "a b")
Utils.assert_eq(fn("a b c"), "a b c c")
Utils.assert_eq(fn("a b c d e"), "a b c d e e c d e e")
Utils.assert_eq(fn(" a b"), " a b b")
Utils.assert_eq(fn("a b "), "a b  ")
Utils.assert_eq(fn("( a b) c"), " a b b c")
Utils.assert_eq(fn("(a b ) c"), "a b   c")
Utils.assert_eq(fn("a (b c)"), "a b c")
Utils.assert_eq(fn("a !(b c)"), "a (b c c")
Utils.assert_eq(fn("() a (() b c)"), " a  b c c  b c c")
Utils.assert_eq(fn("(a b) c d"), "a b c d d")
Utils.assert_eq(fn("a b c d"), "a b c d c d")
Utils.assert_eq(fn("a (b (c (d"), "a b c d")
Utils.assert_eq(fn("() !c !!d"), " c !d !d")

let level: Types.level = {
  name: "please",
  fn: fn,
  goal: "a (short) damned message, pretty pretty please!!",
  answer: "a (!(short!) (damned (message, (pretty (pretty (please!!!!",
}

