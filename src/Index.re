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

let levels: array(Types.level) = [|
  {
    name: "id",
    goal: "a damned message",
    answer: "a damned message",
    fn: (x) => x,
  },
  {
    name: "trim",
    goal: "a damned message",
    answer: "a damned message...",
    fn: (x) => String.sub(x, 0, max(0, String.length(x) - 3)),
  },
  Rotate.level,
  Extend.level,
  Unary.level,
  Cancer.level,
  Milk.level,
  Book.level,
|]

Array.map((level: Types.level) => {
  let result = level.fn(level.answer);
  (result == level.goal) ? "" : {
    Js.log(level.name ++ ": " ++ result);
    Js.Exn.raiseError("Level answer error")
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
    | None => { solved: Js.Dict.empty(), level: 0, }
    | Some(save_state) => parseIntoMyData(save_state)
    // try (
    // parseIntoMyData(save_state)
    //   ) {
    //   | _ -> { solved: Js.Dict.empty(), level: 0 }
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
