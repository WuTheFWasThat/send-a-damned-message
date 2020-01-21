let fn = (x) => {
  x |> Utils.map_words((w) => {
      let l = String.length(w);
      if (l == 0) {
        w
      } else {
        String.sub(w, l-1, 1) ++ String.sub(w, 0, l-1)
      }
  })
}

let level: Types.level = {
  name: "pins",
  goal: "a damned message",
  answer: "a amnedd essagem",
  fn: fn,
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("  "), "  ")
Utils.assert_eq(fn("blah"), "hbla")
// Utils.assert_eq(fn("blah "), " hbla")
// Utils.assert_eq(fn("blah ab "), " hbla ba")
Utils.assert_eq(fn("blah ab "), "hbla ba ")
// Utils.assert_eq(fn("a$df ab cd ehh"), "heh fa$d ba dc")
Utils.assert_eq(fn("a$df ab cd ehh"), "a$fd ba dc heh")
