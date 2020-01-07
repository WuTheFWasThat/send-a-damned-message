let fn = (x) => {
  switch (String.contains(x, ' ')) {
  | false => ""
  | true =>
    let i = String.index(x, ' ');
    let book = String.sub(x, 0, i);
    let code = String.sub(x, i+1, String.length(x)-i-1);
    // Js.log("book: " ++ book ++ " code: " ++ code);
    String.map(
      l =>
      Utils.is_alphabet(l) ?  String.get(book, Utils.a2num(l) mod String.length(book)) : l,
      code
    )
  }
}

let level: Types.level = {
  name: "book",
  fn: fn,
  goal: "a damned message",
  // answer: "adamnedmessage a bcdefg hijklmn",
  answer: "abcdefghijklmnopqrs a damned message",
}
