let fn = (x) => {
  let n = String.length(x);
  switch (Utils.safe_index(x, 's')) {
    | None => ""
    | Some(i) => { String.sub(x, i+1, n-i-1) ++ String.sub(x, 0, i) }
  }
}

let level: Types.level = {
  name: "end",
  old_names: [],
  fn: fn,
  goal: "end all the damned messages",
  answer: "send all the damned messages",
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("abracadabra"), "")
Utils.assert_eq(fn("ass"), "sa")
Utils.assert_eq(fn("sass"), "ass")
Utils.assert_eq(fn("agess"), "sage")
Utils.assert_eq(fn("send"), "end")
