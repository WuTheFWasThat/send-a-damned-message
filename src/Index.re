// Entry point

[@bs.val] external document: Js.t({..}) = "document";

// We're using raw DOM manipulations here, to avoid making you read
// ReasonReact when you might precisely be trying to learn it for the first
// time through the examples later.
let style = document##createElement("style");
document##head##appendChild(style);
style##innerHTML #= Styles.style;

let makeContainer = () => {
  let div = document##createElement("div");
  div##className #= "react-main";
  let () = document##body##appendChild(div);
  div;
};

// LEVEL IDEAS
// - cumulative xor?
// - compress from 2N in natural way?  something where you have to solve lp?  like xor of 3 positions type of thing
//     - maybe there are 2^n positions.  then each position reads from places where nth bit is 1

// SEND
// Age
// Dang
// *Ancer
// Milk
// Nary (uNwary)
// Ext
// Def
// Mum
// Emend
// Super (caps)
//
//
//
// End

// Book.level,
// Crypt.level,
// Hike.level,
// Tricky.level,
// Please.level,
// Madden.level,

let levels: array(Types.level) = [|
  {
    name: "send",
    old_names: [],
    goal: "a damned message",
    answer: "a damned message",
    fn: (x) => x,
  },
  {
    name: "mess",
    old_names: [],
    goal: "a damned message",
    answer: "a damned message...",
    fn: (x) => String.sub(x, 0, max(0, String.length(x) - 3)),
  },
  Pins.level,
  Cancer.level,
  Extend.level,
  Unary.level,
  Milk.level,
  Caps.level,
  Meme.level,
  Mum.level,
  Book.level,
  Crypt.level,
  Hike.level,
  Swiss.level,
  Let.level,
  Bin.level,
  Tricky.level,
  Madden.level,
  Please.level,
  Emend.level,
  Onion.level,
  End.level,
|]

Array.map((level: Types.level) => {
  let result = level.fn(level.answer);
  (result == level.goal) ? "" : {
    Js.log(level.name ++ ": " ++ result);
    Js.Exn.raiseError("Level '" ++ level.name ++ "' answer error")
  }
}, levels);

let saveLocalState: (Types.savestate) => unit = save_state => switch (Js.Json.stringifyAny(save_state)) {
  | None => ()
  | Some(stringified_save_state) =>
    Dom.Storage.(
      localStorage |> setItem("state", stringified_save_state)
    )
};

[@bs.scope "JSON"] [@bs.val]
external parseIntoMyData : string => Types.savestate = "parse";

let loadLocalState: (unit) => Types.savestate = () => {
  switch (Dom.Storage.(localStorage |> getItem("state"))) {
    | None => { answers: Js.Dict.empty(), level: 0, }
    | Some(save_state) => parseIntoMyData(save_state)
    // try (
    // parseIntoMyData(save_state)
    //   ) {
    //   | _ -> { answers: Js.Dict.empty(), level: 0 }
    // }
  }
}

ReactDOMRe.render(
  <SendMessageComponent levels={levels} savedstate={loadLocalState()} savestate={saveLocalState}/>,
  makeContainer(),
);

// TODO: make this less ugly
[%raw {|
  window.onerror = function (message, file, line, col, error) {
     alert("Error occurred!  Please file a github issue with the level and string entered!\n" + error.message)
     return false
  }
|}];

[%raw {|
  window.addEventListener("error", function (e) {
     alert("Error occurred!  Please file a github issue with the level and string entered!\n" + e.error.message)
     return false
  })
|}];
