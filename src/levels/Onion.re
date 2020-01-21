let fn = (x) => {
  let rec cut = (s) => {
    let n = String.length(s);
    if (n == 0) {
      s
    } else {
      let letter = String.get(s, 0);
      switch (Utils.safe_index(s, letter, ~from=1)) {
        | None => Char.escaped(letter) ++ cut(String.sub(s, 1, n-1))
        | Some(i) => {
          Char.escaped(letter) ++ cut(
            Utils.reverse_str(String.sub(s, 1, i-1)) ++ String.sub(s, i, n-i)
          )
        }
      }
    }
  }
  cut(x)
}

/*
To solve:
key: swaps happen in order of output messgae
a damees
working backwards

a damned message
ssage --> want this before swapping S, gives "ssage"
egasse --> want this before swapping E, gives "essage"
em1'egasse --> want this before swapping E, gives "e1message"
menm1'egasse --> want this before swapping M, gives "mne1message"
age1mnemasse --> want this before swapping A, gives "amne1message"
degad mnemasse --> want this before swapping D, gives "damned message"
 daged mnemasse --> want this before swapping space, gives "damned message"
ad aged mnemasse --> want this before swapping space, gives "damned message"
*/

let level: Types.level = {
  name: "onion", // onion, salsa
  fn: fn,
  goal: "a damned message",
  answer: "ad aged mnemasse",
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "a")
Utils.assert_eq(fn("abba"), "abba")
Utils.assert_eq(fn("baab"), "baab")
Utils.assert_eq(fn("abab"), "abab")
Utils.assert_eq(fn("sand"), "sand")
Utils.assert_eq(fn("sanadweeb"), "sanadweeb")
Utils.assert_eq(fn("sanadweneb"), "sanenadweb")
Utils.assert_eq(fn("sanadnweeb"), "sandanweeb")
Utils.assert_eq(fn("sanmadnweeb"), "samndanweeb")
Utils.assert_eq(fn("bsanmadnweeb"), "beewnmandasb")
Utils.assert_eq(fn("bsanmadnweebanb"), "beewnmanasbndab")
Utils.assert_eq(fn("eeabea"), "eebaea")
