let rec range = (start: int, end_: int) => {
  if (start >= end_) {
    [];
  } else {
    [start, ...range(start + 1, end_)];
  };
}

let unwrap_or = (x: option('a), default: 'a) => {
  switch (x) { | None => default | Some(y) => y }
}

let unwrap = (x: option('a)) => {
  switch (x) { | None => Js.Exn.raiseError("Failed to unwrap!") | Some(y) => y }
}

let assert_true: (~msg: string=?, bool) => unit = (~msg="Assertion error", x) => {
  x ? () : {
    Js.log("Assertion error: " ++ msg);
    Js.Exn.raiseError("Assertion error: " ++ msg)
  };
}

let assert_eq: (~msg: string=?, 'a, 'a) => unit = (~msg="", x, y) => {
  assert_true(x == y, ~msg=msg ++ "expected '" ++ unwrap(Js.Json.stringifyAny(x)) ++ "' == '" ++ unwrap(Js.Json.stringifyAny(y)) ++ "'");
}

// let safe_get = (l: list('a), i: int): option('a) => {
let safe_get = (l: string, i: int): option(char) => {
  let n = String.length(l);
  if (i < n && i >= 0) { Some(String.get(l, i)) } else { None }
}
let safe_get_array = (l: array('a), i: int): option('a) => {
  let n = Array.length(l);
  if (i < n && i >= 0) { Some(Array.get(l, i)) } else { None }
}
let safe_get_list = (l: list('a), i: int): option('a) => {
  let n = List.length(l);
  if (i < n && i >= 0) { Some(List.nth(l, i)) } else { None }
}

let char_list: (string) => list(char) = (s) => List.init(String.length(s), String.get(s));
let join_char_list: (list(char)) => string = (l) => l |> Array.of_list |> Array.map((x) => Char.escaped(x)) |>  Js.Array.joinWith("");
let reverse_str = (x: string) => { x |> char_list |> List.rev |> join_char_list }

let filter_none: (list(option('a))) => list('a) = (l) => List.map((x) => unwrap(x), List.filter((x) => x != None, l));

let alphabet = "abcdefghijklmnopqrstuvwxyz"

let is_alphabet = (l) => String.contains(alphabet, Char.lowercase_ascii(l))

let vowels = "aeiou"
let is_vowel = (l) => String.contains(vowels, Char.lowercase_ascii(l))

let consonants = "bcdfghjklmnpqrstvwxyz"
let is_consonant = (l) => String.contains(consonants, Char.lowercase_ascii(l))

let a2num = (~with_spaces=false, x: char) => {
  switch (with_spaces && (x == ' ')) {
    | true => 0
    | false => String.index(alphabet, Char.lowercase_ascii(x)) + (with_spaces ? 1 : 0)
  }
}

assert_eq(a2num('A', ~with_spaces=true), 1);
assert_eq(a2num('A', ~with_spaces=false), 0);
assert_eq(a2num('z', ~with_spaces=true), 26);
assert_eq(a2num('z', ~with_spaces=false), 25);
assert_eq(a2num(' ', ~with_spaces=true), 0);

let num2a = (~with_spaces=false, n: int) => {
  switch (with_spaces && (n == 0)) {
    | true => ' '
    | false => String.get(alphabet, n - (with_spaces ? 1 : 0))
  }
}

assert_eq(num2a(1, ~with_spaces=true), 'a');
assert_eq(num2a(0, ~with_spaces=false), 'a');
assert_eq(num2a(26, ~with_spaces=true), 'z');
assert_eq(num2a(25, ~with_spaces=false), 'z');
assert_eq(num2a(0, ~with_spaces=true), ' ');

let positive_mod = (a, b) => {
  ((a mod b) + b) mod b
};

let cased_like = (x, y) => {
  if (y == Char.uppercase_ascii(y)) { Char.uppercase_ascii(x) } else { x };
}

let rotate_alphabet = (~with_spaces=false, x: char, direction: int) => {
  // Js.log("rotating " ++ Char.escaped(x));
  // Js.log(direction);
  let new_num = positive_mod(a2num(x, ~with_spaces=with_spaces) + direction, with_spaces ? 27 : 26)
  let new_x = num2a(new_num, ~with_spaces=with_spaces)
  cased_like(new_x, x)
};

assert_eq(rotate_alphabet('a', 25), 'z');
assert_eq(rotate_alphabet('A', 25), 'Z');
assert_eq(rotate_alphabet('A', 26, ~with_spaces=true), ' ');
assert_eq(rotate_alphabet('a', 26), 'a');
assert_eq(rotate_alphabet('A', 26), 'A');
assert_eq(rotate_alphabet('a', 27), 'b');
assert_eq(rotate_alphabet('A', 27), 'B');
assert_eq(rotate_alphabet(' ', 3, ~with_spaces=true), 'C');

let first_true: ('a => bool, list('a)) => option('a) = (f, l) => {
  List.fold_left(
    (result, cur) => {
      switch (result) {
        | Some(x) => Some(x)
        | None => f(cur) ? Some(cur) : None
      }
    },
    None,
    l,
  )
}

type _map_words_state = {
  word: string,
  result: string,
};
let map_words = (f, x) => {
  let s = List.fold_left(
    (s, char) => {
      if (is_alphabet(char)) {
        { result: s.result, word: s.word ++ Char.escaped(char) }
      } else {
        { result: s.result ++ f(s.word) ++ Char.escaped(char), word: "" }
      }
    },
    { word: "", result: "" },
    char_list(x)
  );
  s.result ++ f(s.word)
}

