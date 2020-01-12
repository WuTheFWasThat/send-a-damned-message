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
  let read_quote = (quote: char, i: int): (string, int) => {
    if (i == n) {
      ("", i)
    } else switch(Utils.safe_index(x, quote, ~from=i)) {
      | Some(new_i) => {
        (String.sub(x, i, new_i-i), new_i+1)
      }
      | None => (String.sub(x, i, n-i), n)
    }
  }
  let rec read_words = (s: state): state => {
    if (s.index == n) { s } else {
      let letter = String.get(x, s.index);
      if (letter == ')') {
        { ...s, index: s.index + 1 }
      } else if (letter == ' ') {
        read_words({ word: "", words: List.append(s.words, [s.word]), index: s.index + 1 });
      } else if (letter == '"' || letter == '\'') {
        let (quote_result, new_i) = read_quote(letter, s.index+1);
        read_words({ word: s.word ++ quote_result, words: s.words, index: new_i })
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
    // guaranteed to have at least one word
    let first_word = Array.get(words, 0);
    if (nw == 1) {
      first_word
    } else if (nw == 2 || nw == 3) {
      // a b c -> a a b (c)
      Array.append(Array.of_list([first_word]), words) |> Js.Array.filter(x => String.length(x) > 0) |> Js.Array.joinWith(" ")
    } else {
      let new_word = Array.append(Array.of_list([first_word]), Array.sub(words, 0, 3)) |> Js.Array.filter(x => String.length(x) > 0) |> Js.Array.joinWith(" ");
      process_words(Array.append(
         Array.of_list([new_word]),
         Array.sub(words, 3, nw-3)
      ))
    }
  }

  let s = read_words({word: "", words: [], index: 0});


  process_words(List.append(s.words, [s.word]) |> Array.of_list)
}

Utils.assert_eq(fn("a b"), "a a b")
Utils.assert_eq(fn("a b c"), "a a b c")
Utils.assert_eq(fn("a b c d e"), "a a b c a a b c d e")
Utils.assert_eq(fn(" a b"), "a b")
Utils.assert_eq(fn("\" a b\" c"), " a b  a b c")
Utils.assert_eq(fn(" a ( b c)"), "a b c")
Utils.assert_eq(fn("() a (() b c)"), "a b c")
Utils.assert_eq(fn("(a b) c d"), "a a b a a b c d")
Utils.assert_eq(fn("a b c d"), "a a b c a a b c d")
Utils.assert_eq(fn("\"(a b)\" c d"), "(a b) (a b) c d")
Utils.assert_eq(fn("() \"c\" \"d\""), "c d")
Utils.assert_eq(fn("'\"' \"'\" c"), "\" \" ' c")

let level: Types.level = {
  name: "please",
  fn: fn,
  goal: "(please) send a short \"damned\" message wouldn't you?",
  answer: "() '(please) send a short \"damned\" message' \"wouldn't you?\"",
}
