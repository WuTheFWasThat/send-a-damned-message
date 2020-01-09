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

let a2num: (~with_spaces: bool=?, char) => int = (~with_spaces=false, x) => {
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

let is_alphabet = (l) => String.contains(alphabet, Char.lowercase_ascii(l))

/*
def is_vowel(l):
    return l.lower() in 'aeiou'

def is_consonant(l):
    return l.lower() in 'bcdfghjklmnpqrstvwxyz'

def num2a(n, with_spaces=False):
    if with_spaces and n == 0:
        return ' '
    return chr(n + ord('a') - (1 if with_spaces else 0))

def is_alphabet(l):
    return l.lower() in alphabet

def rotate_alphabet(x, direction, with_spaces=False):
    is_upper = x == x.upper()
    new_x = num2a((a2num(x, with_spaces) + direction) % (27 if with_spaces else 26), with_spaces)
    if is_upper:
        new_x = new_x.upper()
    return new_x
*/
