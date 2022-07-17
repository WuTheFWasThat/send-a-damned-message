let char2numwithcaps = (x) => {
  if (!Utils.is_alphabet(x)) {
    0
  } else if (Utils.is_lower(x)) {
    28 - Utils.char2num(x)
  } else {
    Utils.char2num(x) - 28
  }
}

let fn = (x) => {
  let bigrams = List.map(
    (i) => { (String.get(x, i), String.get(x, i+1)) },
    Utils.range(String.length(x)-1, ~start=0, ~incr=2),
  );
  let winners = List.map(
    (tup) => {
      let (x, y) = tup;
      if (char2numwithcaps(x) < char2numwithcaps(y)) { x } else { y }
    }, bigrams
  );
  let losers = List.map(
    (tup) => {
      let (x, y) = tup;
      if (char2numwithcaps(x) < char2numwithcaps(y)) { y } else { x }
    }, bigrams
  );
  let parts = List.map(
    (i) => {
      let loser = if (i == 0) {
        List.nth(losers, i)
      } else {
        List.nth(winners, i-1)
      };
      let winner = if (i == List.length(winners) - 1) {
        List.nth(winners, i)
      } else {
        List.nth(losers, i+1)
      };
      String.make(1, loser) ++ String.make(1, winner)
    },
    Utils.range(List.length(winners), ~start=0),
  );
  String.lowercase_ascii(String.concat("", parts))
}

let level: Types.level = {
  name: "Swiss",
  old_names: [],
  goal: "a damned message",
  answer: "ad Maen demsSGae",
  fn: fn,
}


Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn(" "), "")
Utils.assert_eq(fn("  "), "  ")
Utils.assert_eq(fn("ba"), "ab")
Utils.assert_eq(fn("ab"), "ab")
Utils.assert_eq(fn("az"), "az")
Utils.assert_eq(fn("Az"), "za")
Utils.assert_eq(fn("AZ"), "za")
Utils.assert_eq(fn("aZ"), "az")
Utils.assert_eq(fn("??"), "??")
Utils.assert_eq(fn("a?"), "a?")
Utils.assert_eq(fn("?a"), "a?")
Utils.assert_eq(fn("abcd"), "acbd")
Utils.assert_eq(fn("dcba"), "cadb")
/* Utils.assert_eq(fn("a damned messgae"), "a damned message") */
