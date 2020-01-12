// This is the ReactJS documentation's useReducer example, directly ported over
// https://reactjs.org/docs/hooks-reference.html#usereducer

// A little extra we've put, because the ReactJS example has no styling
let githubLinkStyle = ReactDOMRe.Style.make(
  ~color="white", ~fontSize="18 px", ~textDecoration="none", ()
);

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
  justsolved: bool,
};

type levelmenustate = Solved | Unlocked | Locked;

type action =
  SendMessage
  | SetMessage(string)
  | SetLevel(int);

let focusInput: (unit) => unit = [%raw {|
  function() {
    setTimeout(() => {
      let input = document.getElementById('main-input');
      if (input) {
        input.focus();
        input.select();
      }
    }, 0)
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
let make = (
  ~levels: array(Types.level), ~savedstate: Types.savestate, ~savestate: (Types.savestate) => unit,
) => {
  let reducer = (state, action) => {
    let newstate = switch (action) {
      | SetMessage(msg) => { ...state, message: msg }
      | SendMessage => {
        let message = state.message;
        let level = levels[state.savedstate.level];
        let damned_message = level.fn(message);
        let solved = damned_message == level.goal;
        if (solved) {
          Js.Dict.set(state.savedstate.answers, level.name, message);
        };
        let attempts = List.append(state.attempts, [{
            message: message, damned: damned_message
        }]);
        { ...state, attempts: attempts, message: message, justsolved: solved };
      }
      | SetLevel(level) => {
        Js.log("setting level: " ++ levels[level].name);
        focusInput();
        {
          message: "", attempts: [], justsolved: false,
          savedstate: { ...state.savedstate, level: level }
        }
      }
    };
    savestate(newstate.savedstate);
    newstate
  };
  let initialState = {
    message: "", attempts: [], savedstate: savedstate,
    justsolved: false,
  };

  let (state, dispatch) = React.useReducer(reducer, initialState);
  Js.log("state: " ++ switch (Js.Json.stringifyAny(state)) { | None => "?" | Some(x) => x } );

  let level_solved = levels |> Array.map((level: Types.level) => {
    switch (Js.Dict.get(state.savedstate.answers, level.name)) {
      | None => false
      // re-verify answer
      | Some(answer) => { level.fn(answer) == level.goal }
    }
  });

  let set_cheat: ((unit) => unit) => unit = [%raw {|
    function(fn) { window.cheat = fn }
  |}];

  let level = levels[state.savedstate.level];
  set_cheat(() => dispatch(SetMessage(level.answer)));

  let nlevels = Array.length(levels);
  let level_state = level_solved |> Array.mapi((i, solved) => {
    if (solved) {
      Solved;
    } else {
      if (i == nlevels - 1) {
        let all_but_last_solved = Array.sub(level_solved, 0, nlevels-1) |> Array.fold_left((x, y) => x && y, true);
        all_but_last_solved ? Unlocked : Locked;
      } else if ((i == 0) ||
          Utils.safe_get_array(level_solved, i-1) == Some(true) ||
          Utils.safe_get_array(level_solved, i-2) == Some(true)
         ) {
        Unlocked;
      } else {
        Locked;
      }
    }
  });

  <div>
  <div style={ReactDOMRe.Style.make(
     ~textAlign="right", ()
  )}>
    <a href="https://github.com/WuTheFWasThat/send-a-damned-message" style={githubLinkStyle}>
      {React.string("View on Github")}
    </a>
  </div>
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
    style={ReactDOMRe.Style.make(~display="flex", ())}>
    <div className="levelselect">
      {
        ReasonReact.array(Array.mapi((i: int, level: Types.level) => {
          let levelstate = Array.get(level_state, i);
          let className = "levelitem";
          let className = className ++ ((i == state.savedstate.level) ? " selectedlevel" : "");
          let className = className ++ ((levelstate == Locked) ? " levellocked" : "");
          let className = className ++ ((levelstate == Unlocked) ? " levelunlocked" : "");
          let className = className ++ ((levelstate == Solved) ? " levelsolved" : "");

          <div
            key={string_of_int(i)}
            className={className }
            onClick={(_ev) => dispatch(SetLevel(i))}
          >
            <div>
              // {React.string(string_of_int(i) ++ ": " ++ level.name)}
              {React.string(level.name)}
            </div>
          </div>
        }, levels))
      }
    </div>
    <div style={ReactDOMRe.Style.make(~flexGrow="1", ~paddingLeft="20px", ())}>
      {
        if (state.justsolved && (state.savedstate.level == nlevels - 1)) {
          <div style={ReactDOMRe.Style.make(~textAlign="center", ())}>
            {React.string("Congratulations!  No more damned messages!")}
          </div>
        } else {
          <div>
            <h3 className="center">
              {React.string("Level " ++ string_of_int(state.savedstate.level) ++ ": " ++ level.name)}
            </h3>
            <div className="messages_container">
              {
                ReasonReact.array(Array.of_list(List.mapi((i: int, attempt: attempt) => {
                  <div className="message_pair" key={string_of_int(i)} >
                    <pre className="undamnedmessage">
                      {React.string(attempt.message)}
                    </pre>
                    <br/>
                    <pre className={(attempt.damned === level.goal) ? "goodmessage" : "damnedmessage"}>
                      {React.string(attempt.damned)}
                    </pre>
                  </div>
                }, state.attempts)))
              }
            </div>
            {
              if (state.justsolved) {
                <button onClick={(_ev) => dispatch(SetLevel(state.savedstate.level + 1))} autoFocus=true>
                  {React.string("Next level!")}
                </button>
              } else {
                <div>
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
              }
            }
          </div>
        }
      }
    </div>
    </div>
    </div>
  </div>
  </div>;
};
