type state = {
  prev: option(char),
  count: int,
  result: string,
};

let fn = (x) => {
  /*
     asterisks bleed, spaces stop it
   */
  let chars = Utils.char_list(x) |> Array.of_list;

  ignore(List.mapi((i, char) => {
    switch (char == '*') {
      | false => ignore()
      | true => {
        ignore(List.map(
          (dir) => {
            if (Utils.safe_get(x, i+dir) != None) {
              Array.set(chars, i+dir, char)
            }
          },
          [-1, 1]
        ))
      }
    }
  }, Utils.char_list(x)))

  chars |> Array.to_list |> Utils.join_char_list
}

let level: Types.level = {
  name: "cancer",
  fn: fn,
  goal: "a d***ed message",
  answer: "a da*ned message",
}

Utils.assert_eq(fn(""), "")
Utils.assert_eq(fn("a a*a c"), "a *** c")
Utils.assert_eq(fn("a *b* c"), "a*****c")
Utils.assert_eq(fn("*bcd* c"), "**c***c")
Utils.assert_eq(fn("ys t**"), "ys ***")
