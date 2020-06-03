/*
let fn = (x) => {
  let k = 3;
  let n = String.length(x);
  let nk = n / k;
  let chars = Array.of_list(Utils.char_list(x));
  Utils.range(nk) |> List.map(i => {
    let inds = Utils.range(k) |> List.map(j => i + nk * j);
    Utils.range(k) |> List.map(j => {
      Array.set(
        chars,
        List.nth(inds, j),
        // natural version but with some stationary chars
        // String.get(x, List.nth(inds, (j + i) mod k))
        String.get(x, List.nth(inds, (j + (if (i mod 2 == 0) { 1 } else { k-1 })) mod k))
      )
    })
  }) |> ignore
  chars |> Utils.join_char_array
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "a")
Utils.assert_eq(fn("ab"), "ab")
Utils.assert_eq(fn("abc"), "bca")
Utils.assert_eq(fn("abcd"), "bcad")
Utils.assert_eq(fn("abcde"), "bcade")
Utils.assert_eq(fn("abcdef"), "cfebad")
Utils.assert_eq(fn("abcdefg"), "cfebadg")
Utils.assert_eq(fn("abcdefgh"), "cfebadgh")
*/

/*
let rec fn = (x) => {
  let k = 3;
  let n = String.length(x);
  let nk = n / k;
  if (n < k) {
    x
  } else {
    let substrs = Utils.range(k) |> List.map(i => {
      fn(String.sub(x, i * nk, nk))
    });
    let remainder = String.sub(x, nk * k, n - (nk * k));
    String.concat("", List.append(
      List.tl(substrs), [List.hd(substrs), remainder]
    ))
  }
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "a")
Utils.assert_eq(fn("ab"), "ab")
Utils.assert_eq(fn("abc"), "bca")
Utils.assert_eq(fn("abcd"), "bcad")
Utils.assert_eq(fn("abcde"), "bcade")
Utils.assert_eq(fn("abcdef"), "cdefab")
Utils.assert_eq(fn("abcdefg"), "cdefabg")
Utils.assert_eq(fn("abcdefgh"), "cdefabgh")
Utils.assert_eq(fn("abcdefghi"), "efdhigbca")
*/

let fn = (x) => {
  let k = 3;
  let n = String.length(x);
  let nk = n / k;
  let result = Utils.range(nk) |> List.map(i => {
    String.sub(x, i*k+1, k-1) ++ String.sub(x, i*k , 1)
  }) |>  String.concat("")
  result ++ String.sub(x, nk * k, n - (nk * k))
}


Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a"), "a")
Utils.assert_eq(fn("ab"), "ab")
Utils.assert_eq(fn("abc"), "bca")
Utils.assert_eq(fn("abcd"), "bcad")
Utils.assert_eq(fn("abcde"), "bcade")
Utils.assert_eq(fn("abcdef"), "bcaefd")
Utils.assert_eq(fn("abcdefg"), "bcaefdg")
Utils.assert_eq(fn("abcdefgh"), "bcaefdgh")
Utils.assert_eq(fn("abcdefghi"), "bcaefdhig")
List.map(length => {
  let s = Utils.rand_string(length);
  Utils.assert_eq(fn(fn(fn(s))), s);
}, Utils.range(20))

let goal = "a damned message which is way too damned long and confusing, as a sanctimonious man, in an attempt to separate the damned from the virutous, damned it to contain \"damned\" as an adjective, noun, adverb, and verb; the damned use brute force and forever hold guilt in their chest, while the virtuous condemn them repeatedly and effortlessly find the key to enlightenment";
let level: Types.level = {
  name: "tricky",
  fn: fn,
  goal: goal,
  answer: fn(fn(goal)),
}

