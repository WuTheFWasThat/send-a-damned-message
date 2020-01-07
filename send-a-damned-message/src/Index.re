// Entry point

[@bs.val] external document: Js.t({..}) = "document";

// We're using raw DOM manipulations here, to avoid making you read
// ReasonReact when you might precisely be trying to learn it for the first
// time through the examples later.
let style = document##createElement("style");
document##head##appendChild(style);
style##innerHTML #= Styles.style;

let makeContainer = text => {
  let div = document##createElement("div");
  let () = document##body##appendChild(div);
  div;
};

let levels: array(Types.level) = [|
  {
    name: "id",
    goal: "a damned message",
    fn: (x) => x,
  },
  {
    name: "trim",
    goal: "a damned message",
    fn: (x) => String.sub(x, 0, max(0, String.length(x) - 3)),
  },
|]

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
  <SendMessageComponent levels={levels} savestate={loadLocalState()}/>,
  makeContainer("Send A Damned Message"),
);
