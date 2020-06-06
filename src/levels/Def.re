type _state = {
  words: list(string),
  word: string,
  all_whitespace: bool,
}

type def = {
  k: string,
  v: string
};
type _state2 = {
  words: list(string),
  word: string,
  all_whitespace: bool,
}

let apply_defs = (defs: list(def), s) => {
  List.fold_left((s, def) => {
    Utils.assert_true(String.length(def.k) > 0);
    Utils.replace_all(s, def.k, def.v)
  }, s, defs);
}

let fn = (x) => {
  /*
   sequence of definitions
  */
  let s = List.fold_left((s, char) => {
    if ((char == ' ') && !s.all_whitespace) {
      {
        words: List.append(s.words, [s.word]),
        word: "", all_whitespace: true
      }
    } else {
      {
        words: s.words,
        word: s.word ++ String.make(1, char),
        all_whitespace: (s.all_whitespace && (char == ' ')),
      }
    }
  }, { words: [], word: "", all_whitespace: true }, Utils.char_list(x));

  let words = Array.of_list(List.append(s.words, [s.word]));
  let n = Array.length(words);

  if (n mod 2 == 0) {
    ""
  } else {
    let defs = Array.fold_left((defs, i) => {
      let k = words[i];
      let v = apply_defs(defs, words[i+1]);
      List.append(defs, [{k: k, v: v}])
    }, [], Array.of_list(Utils.range(n-1, ~incr=2)));

    apply_defs(defs, words[n-1]);
  }
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("b a c b c"), "a")
Utils.assert_eq(fn("b  a c b c"), " a")
Utils.assert_eq(fn("b a c b cab"), "aaa")
Utils.assert_eq(fn("b c c b cab"), "cac")
Utils.assert_eq(fn("b  a c  b abc"), "a a  a")
Utils.assert_eq(fn(" b  a c  b abc"), "ab a")
Utils.assert_eq(fn(" b  a b"), "b")
Utils.assert_eq(fn("a b c"), "c")
Utils.assert_eq(fn("a b c "), "")
Utils.assert_eq(fn("a  "), "")
Utils.assert_eq(fn("a b"), "")
Utils.assert_eq(fn("a b "), "")
Utils.assert_eq(fn("a b  "), " ")
Utils.assert_eq(fn("a fat fat b a"), "b")

let level: Types.level = {
  name: "def",
  old_names: ["let"],
  fn: fn,
  goal: "a  damned  message",
  answer: "x   d y   m axamnedyessage",
}

