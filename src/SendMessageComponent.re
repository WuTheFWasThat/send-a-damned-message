// This is the ReactJS documentation's useReducer example, directly ported over
// https://reactjs.org/docs/hooks-reference.html#usereducer

// A little extra we've put, because the ReactJS example has no styling
let leftButtonStyle = ReactDOMRe.Style.make(~borderRadius="4px 0px 0px 4px", ~width="48px", ());
let rightButtonStyle = ReactDOMRe.Style.make(~borderRadius="0px 4px 4px 0px", ~width="48px", ());

type attempt = {
  message: string,
  damned: string,
};
// Record and variant need explicit declarations.
type state = {
  message: string,
  // TODO: keep a list per level?
  attempts: list(attempt),
  savedstate: Types.savestate,
};

type action =
  SendMessage
  | SetMessage(string)
  | SetLevel(int);

let focusInput: (unit) => unit = [%raw {|
  function() {
    let input = document.getElementById('main-input');
    input.focus();
    input.select();
  }
|}];

[%raw {|
  window.onload = function () {
    focusInput()
    // setInterval(() => {
    //   focusInput();
    // }, 1000);
  }
|}];

[@react.component]
let make = (~levels: array(Types.level), ~savedstate: Types.savestate, ~savestate: (Types.savestate) => unit) => {
  let reducer = (state, action) => {
    let newstate = switch (action) {
      | SetMessage(msg) => { ...state, message: msg }
      | SendMessage => {
        let message = state.message;
        let level = levels[state.savedstate.level];
        let damned_message = level.fn(message);
        let attempt = {
          message: message, damned: damned_message
        };
        {
          ...state,
          attempts: List.append(state.attempts, [attempt]), message: ""
        };
      }
      | SetLevel(level) => {
        Js.log("setting level: " ++ levels[level].name);
        focusInput();
        {
          ...state,
          attempts: [],
          savedstate: {
            ...state.savedstate,
            level: level
          }
        }
      }
    };
    savestate(newstate.savedstate);
    newstate
  };
  let initialState = { message: "", attempts: [], savedstate: savedstate, };

  let (state, dispatch) = React.useReducer(reducer, initialState);
  Js.log("state: " ++ switch (Js.Json.stringifyAny(state)) { | None => "?" | Some(x) => x } );
  let level = levels[state.savedstate.level];

  <div>
  <div className="container">

  <div className="containerTitle">
    {React.string("Send A ")}
    <span className="damnedmessage">
    {React.string("Damned")}
    </span>
    {React.string(" Message")}
  </div>

  <div className="containerContent">
  <div
    style={ReactDOMRe.Style.make(~display="flex", ~alignItems="center", ~justifyContent="space-between", ())}>
    <div className="levelselect">
      {
        ReasonReact.array(Array.mapi((i: int, level: Types.level) => {
          <div
            key={string_of_int(i)}
            className={"levelitem" ++ ((i == state.savedstate.level) ? " selectedlevel" : "") }
            onClick={(_ev) => dispatch(SetLevel(i))}
          >
            <div>
              {React.string(string_of_int(i) ++ ": " ++ level.name)}
            </div>
          </div>
        }, levels))
      }
    </div>
    <div style={ReactDOMRe.Style.make(~flexGrow="1", ~padding="20px", ())}>
      <h3 className="center">
        {React.string("Level " ++ string_of_int(state.savedstate.level) ++ ": " ++ level.name)}
      </h3>
      {
        ReasonReact.array(Array.of_list(List.mapi((i: int, attempt: attempt) => {
          <div key={string_of_int(i)}>
            <div>
              <pre className="undamnedmessage">
                {React.string(attempt.message)}
              </pre>
            </div>
            <div>
              <pre className={(attempt.damned === level.goal) ? "goodmessage" : "damnedmessage"}>
                {React.string(attempt.damned)}
              </pre>
            </div>
          </div>
        }, state.attempts)))
      }
      <div style={ReactDOMRe.Style.make(~fontWeight="bold", ())}>
        {React.string("Goal is to send: ")}
        <pre className="goodmessage">
        {React.string(level.goal)}
        </pre>
      </div>
      <form className="fullwidth" onSubmit={event => {
        Js.log("sending message: " ++ state.message);
        ReactEvent.Form.preventDefault(event);
        dispatch(SendMessage);
      }}>
      <div>
        <input id="main-input" className="fullwidth" type_="text" value={state.message} onChange={event => dispatch(SetMessage(event->ReactEvent.Form.target##value))}>
        </input>
      </div>
      </form>
    </div>
    </div>
    </div>
  </div>
  <a href="https://github.com/WuTheFWasThat/send-a-damned-message">{React.string("View code on Github")}</a>
  </div>;
};
