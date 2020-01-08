let fn = (x) => {
  let parts = x |> Js.String.split(" ");
  let words = Array.map(
    part => {
      let l = String.length(part);
      l == 0 ? part : String.sub(part, l-1, 1) ++ String.sub(part, 0, l-1)
    }
  , parts)

  let l = Array.length(words);
  Array.concat([
     Array.sub(words, l-1, 1),
     Array.sub(words, 0, l-1),
  ]) |>  Js.Array.joinWith(" ")
}

let level: Types.level = {
  name: "rot",
  goal: "a damned message",
  answer: "amnedd essagem a",
  fn: fn,
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("  "), "  ")
Utils.assert_eq(fn("blah"), "hbla")
Utils.assert_eq(fn("blah "), " hbla")
Utils.assert_eq(fn("blah ab "), " hbla ba")
Utils.assert_eq(fn("a$df ab cd ehh"), "heh fa$d ba dc")
