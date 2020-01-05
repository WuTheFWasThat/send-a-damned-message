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

let level: Types.level = {
  name: "id",
  goal: "a damned message",
  fn: (x) => x,
}
let level: Types.level = {
  name: "trim",
  goal: "a damned message",
  fn: (x) => String.sub(x, 0, max(0, String.length(x) - 3)),
}
ReactDOMRe.render(
  <SendMessageComponent level={level}/>,
  makeContainer("Send A Damned Message"),
);
