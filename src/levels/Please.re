type state = {
  word: string,
  words: list(string),
  index: int,
};

let rec _eval_words = (s: state): string => {
    let a = s.word;
    switch (Utils.safe_get_list(s.words, s.index)) {
      | None => a
      | Some(b) => {
        switch (Utils.safe_get_list(s.words, s.index+1)) {
          | None => {
            a ++ b ++ " " ++ a
          }
          | Some(c) => {
            _eval_words({
              word: a ++ b ++ " " ++ a ++ c,
              words: s.words,
              index: s.index+2
            })
          }
        }
      }
    }
}

let eval_words = (words: list(string)): string => {
  /* Js.log(words |> Js.Json.stringifyAny); */
  switch (Utils.safe_get_list(words, 0)) {
    | None => "";
    | Some(word) => {
      _eval_words({word: word, words: words, index: 1})
    }
  }
}

let n_dolls_str = (n: int): string => {
  Utils.join_char_list(List.map( (_c) => '$', Utils.range(n)))
}

type _map_words_state = {
  cur: list(string),
  result: list(list(string)),
};
let split_arr = (arr, sep): list(list(string)) => {
  let s = List.fold_left(
    (s, el) => {
      if (el == sep) {
        { cur: [], result: List.append(s.result, [s.cur]) }
      } else {
        { cur: List.append(s.cur, [el]), result: s.result }
      }
    },
    {cur: [], result: []},
    arr,
  );
  List.append(s.result, [s.cur])
}

let rec parse = (words, n_dolls): string => {
    if (n_dolls == 0) {
      eval_words(words)
    } else {
      let new_words = List.map(
        (w) => parse(w, n_dolls - 1),
        split_arr(words, n_dolls_str(n_dolls))
      )
      eval_words(new_words)
    }
}


let fn = (x) => {
  /*
    Ternary operator, a b c -> ab ac
  */
  let w = Utils.split(x, ' ');
  /* Js.log("here " ++ x); */
  /* Js.log("here2 " ++ Utils.unwrap(w |> Js.Json.stringifyAny)); */
  let n_dolls = List.fold_left(
    (n, w) => {
      switch (w == n_dolls_str(String.length(w))) {
        | true => max(String.length(w), n)
        | false => n
      }
    },
    0,
    w
  );
  parse(w, n_dolls)
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "a")
Utils.assert_eq(fn(" a"), "a ")
Utils.assert_eq(fn("a b"), "ab a")
Utils.assert_eq(fn("a b c"), "ab ac")
Utils.assert_eq(fn("a b c d"), "ab acd ab ac")
Utils.assert_eq(fn("a b c d e"), "ab acd ab ace")
Utils.assert_eq(fn(" a b"), "a b")
Utils.assert_eq(fn("a b "), "ab a")

let level: Types.level = {
  name: "please",
  old_names: [],
  fn: fn,
  goal: "pretty pretty please just send a short damned message and maybe some money",
  answer: "$$$$ $$$ $$ $ pretty $ pretty $$ $ please $ just $$$ $$ $ send $ a $$ $ short $ damned $$$$ $$$ $ message $ and $$$ $$ $ maybe $ some $$ money",
}

