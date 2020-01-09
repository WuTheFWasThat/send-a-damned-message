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

let alphabet = "abcdefghijklmnopqrstuvwxyz"

let is_alphabet = (l) => String.contains(alphabet, Char.lowercase_ascii(l))

let is_vowel = (l) => String.contains("aeiou", Char.lowercase_ascii(l))

let is_consonant = (l) => String.contains("bcdfghjklmnpqrstvwxyz", Char.lowercase_ascii(l))

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

let rotate_alphabet = (~with_spaces=false, x: char, direction: int) => {
    let is_upper = x == Char.uppercase_ascii(x)
    let new_x = num2a((a2num(x, ~with_spaces=with_spaces) + direction) mod (with_spaces ? 27 : 26), ~with_spaces=with_spaces)
    is_upper ? Char.uppercase_ascii(new_x) : new_x;
}

assert_eq(rotate_alphabet('a', 25), 'z');
assert_eq(rotate_alphabet('A', 25), 'Z');
assert_eq(rotate_alphabet('A', 26, ~with_spaces=true), ' ');
assert_eq(rotate_alphabet('a', 26), 'a');
assert_eq(rotate_alphabet('A', 26), 'A');
assert_eq(rotate_alphabet('a', 27), 'b');
assert_eq(rotate_alphabet('A', 27), 'B');
assert_eq(rotate_alphabet(' ', 3, ~with_spaces=true), 'C');
