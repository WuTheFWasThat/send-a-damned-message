type state = {
  word: string,
  words: list(string),
  index: int,
};

let maybe_sep = (a: string, b: string, sep: string): string => {
  if (a == "") {
    b
  } else if (b == "") {
    a
  } else {
    a ++ sep ++ b
  }
}

let rec _eval_words = (s: state, sep: string): string => {
  let a = s.word;
  switch (Utils.safe_get_list(s.words, s.index), Utils.safe_get_list(s.words, s.index + 1)) {
    | (None, _) => a
    | (Some(""), None) => a
    | (Some(b), None) => {
      maybe_sep(maybe_sep(a, b, sep), a, sep)
    }
    | (Some(b), Some(c)) => {
      let next = maybe_sep(maybe_sep(a, b, sep), maybe_sep(a, c, sep), sep);
      switch (Utils.safe_get_list(s.words, s.index + 2)) {
        | None => next
        | Some(_d) =>
          _eval_words({word: next, words: s.words, index: s.index + 2}, sep)
      }
    }
  }
}

let eval_words = (words: list(string), sep: string): string => {
  /* Js.log(words |> Js.Json.stringifyAny); */
  switch (Utils.safe_get_list(words, 0)) {
    | None => "";
    | Some(word) => {
      _eval_words({word: word, words: words, index: 1}, sep)
    }
  }
}

let n_dolls_str = (n: int): string => {
  Utils.join_char_list(List.map( (_c) => '$', Utils.range(n)))
}

let rec _consume_dollars = (chars, count) => {
  switch (chars) {
    | [] => (count, [])
    | [c, ...rest] =>
      if (c == '$') {
        _consume_dollars(rest, count + 1)
      } else {
        (count, chars)
      }
  }
}

let rec max_dollar_run = (chars, cur, best) => {
  switch (chars) {
    | [] => best
    | [c, ...rest] =>
      if (c == '$') {
        let cur2 = cur + 1;
        max_dollar_run(rest, cur2, max(cur2, best))
      } else {
        max_dollar_run(rest, 0, best)
      }
  }
}

let rec split_on_run = (chars, run_len, cur, parts) => {
  switch (chars) {
    | [] => List.append(parts, [cur])
    | [c, ...rest] =>
      if (c == '$') {
        let (count, remaining) = _consume_dollars(chars, 0);
        if (count == run_len) {
          split_on_run(
            remaining,
            run_len,
            "",
            List.append(parts, [cur])
          )
        } else {
          split_on_run(remaining, run_len, cur ++ n_dolls_str(count), parts)
        }
      } else {
        split_on_run(rest, run_len, cur ++ String.make(1, c), parts)
      }
  }
}

let rec fn = (s) => {
  let chars = Utils.char_list(s);
  let max_run = max_dollar_run(chars, 0, 0);
  if (max_run == 0) {
    eval_words(Utils.split(s, ' '), " ")
  } else {
    let parts = split_on_run(chars, max_run, "", []);
    let parsed_parts = List.map(fn, parts);
    eval_words(parsed_parts, " ")
  }
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "a")
Utils.assert_eq(fn(" a"), "a")
Utils.assert_eq(fn(" "), "")
Utils.assert_eq(fn("a "), "a")
Utils.assert_eq(fn("a b"), "a b a")
Utils.assert_eq(fn("a b c"), "a b a c")
Utils.assert_eq(fn("a b c d"), "a b a c d a b a c")
Utils.assert_eq(fn("a b c d e"), "a b a c d a b a c e")
Utils.assert_eq(fn(" a b"), "a b")
Utils.assert_eq(fn("a b "), "a b a")
Utils.assert_eq(fn("a  b"), "a a b")
Utils.assert_eq(fn("a  "), "a a")
Utils.assert_eq(fn("$a"), "a")
Utils.assert_eq(fn("a$"), "a")
Utils.assert_eq(fn("a$$"), "a")
Utils.assert_eq(fn("a$$ $$"), "a a")
Utils.assert_eq(fn("$$a"), "a")
Utils.assert_eq(fn("$$ "), "")
Utils.assert_eq(fn("a$$b"), "a b a")
Utils.assert_eq(fn("a$b "), "a b a")
Utils.assert_eq(fn("a$b  "), "a b b a")
Utils.assert_eq(fn("a$$b "), "a b a")
Utils.assert_eq(fn("a$$b c"), "a b c b a")
Utils.assert_eq(fn("a$b c"), "a b c b a")
Utils.assert_eq(fn("ab$c"), "ab c ab")
Utils.assert_eq(fn("a$$b$c"), "a b c b a")
Utils.assert_eq(fn("a$$ b$c"), "a b c b a")
Utils.assert_eq(fn("a$b$c"), "a b a c")
Utils.assert_eq(fn("a $ b $ c"), "a b a c")
Utils.assert_eq(fn("$$ $ a $$ $b$c"), "a b c")


let level: Types.level = {
  name: "plea$e",
  old_names: ["please"],
  fn: fn,
  goal: "pretty pretty please just send a short d!@#ed message and maybe some dollars",
  answer: "$$$$ $$$ $$ $ pretty $ pretty $$ $ please $ just $$$ $$ $ send $ a $$ $ short $ d!@#ed $$$$ $$$ $ message $ and $$$ $$ $ maybe $ some $$ dollars",
}
