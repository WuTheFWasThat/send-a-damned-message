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
  // index (negatively) into attempts, upon "up" becomes -1, basically
  message_cursor: int,
  message_saved: string,
  savedstate: Types.savestate,
  justsolved: bool,
};

type levelmenustate = Solved | Unlocked | Locked;

type action =
  SendMessage
  | SetMessageCursor(int)
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

let set_cheat_all: ((unit) => unit) => unit = [%raw {|
  function(fn) { window.cheat_all = function() { fn(); window.location.reload() }; }
|}];

let set_print_all: ((unit) => unit) => unit = [%raw {|
  function(fn) { window.print_all = function() { fn(); }; }
|}];

let scroll_messages: (unit) => unit = [%raw {|
  function() {
    setTimeout(() => {
      var div = document.getElementById("messages_container");
      div.scrollTop = div.scrollHeight;
    }, 0)
  }
|}];

type titleinfo = {
  prefix: string,
  damned: string,
  suffix: string,
};

[@react.component]
let make = (
  ~levels: array(Types.level), ~savedstate: Types.savestate, ~savestate: (Types.savestate) => unit,
) => {
  let reducer = (state, action) => {
    let newstate = switch (action) {
      | SetMessageCursor(code) => {
          let n = List.length(state.attempts);
          let change = if (code == 38) { 1 // up
          } else if (code == 40) { -1 // down
          } else { 0 };

          let new_cursor = state.message_cursor + change;
          // wasn't even an up or down
          if (change == 0) { state }
          // tried to go up too far
          else if (new_cursor > n) { state }
          // tried to go down too far
          else if (new_cursor < 0) { state }
          // actual change!
          else {
            let saved = if (state.message_cursor == 0) {
              // save the message!
              state.message
            } else {
              state.message_saved
            }
            if (new_cursor == 0) {
              // restore saved message
              {... state, message_cursor: 0, message: state.message_saved }
            } else {
              let old_message = List.nth(state.attempts, n - new_cursor).message;
              {... state, message_cursor: new_cursor, message: old_message, message_saved: saved }
            }
          }
        }
      | SetMessage(msg) => { ...state, message: msg, message_cursor: 0 }
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
        {
          ...state, attempts: attempts,
          message_cursor: 0,
          message: message, justsolved: solved
        };
      }
      | SetLevel(level) => {
        Js.log("setting level: " ++ levels[level].name);
        focusInput();
        {
          message: "", attempts: [], justsolved: false,
          savedstate: { ...state.savedstate, level: level },
          message_cursor: 0, message_saved: "",
        }
      }
    };
    savestate(newstate.savedstate);
    newstate
  };
  let initialState = {
    message: "", attempts: [], savedstate: savedstate,
    justsolved: false,
    message_cursor: 0, message_saved: "",
  };

  let (state, dispatch) = React.useReducer(reducer, initialState);
  Js.log("state: " ++ switch (Js.Json.stringifyAny(state)) { | None => "?" | Some(x) => x } );

  let level_solved = levels |> Array.map((level: Types.level) => {
    List.append(level.old_names, [level.name]) |> List.map(
      name =>
        switch (Js.Dict.get(state.savedstate.answers, name)) {
          | None => false
          // re-verify answer
          | Some(answer) => { level.fn(answer) == level.goal }
        }
    ) |> List.fold_left(
      (a, b) => { a || b }, false
    )
  });

  let set_cheat: ((unit) => unit) => unit = [%raw {|
    function(fn) { window.cheat = fn }
  |}];

  let level = levels[state.savedstate.level];
  set_cheat(() => dispatch(SetMessage(level.answer)));
  set_cheat_all(() => {
    levels |> Array.map((level: Types.level) => {
      Js.Dict.set(state.savedstate.answers, level.name, level.answer);
    }) |> ignore;
    savestate(state.savedstate);
  });
  set_print_all(() => {
    levels |> Array.map((level: Types.level) => {
      "==========================" |> Js.log;
      "Level " ++ level.name ++ "" |> Js.log;
      "Goal: " ++ level.goal |> Js.log;
      "Attempt: " ++ level.fn(level.goal) |> Js.log;
      "Answer: " ++ level.answer |> Js.log;
    }) |> ignore;
  });

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
          Utils.safe_get_array(level_solved, i-2) == Some(true) ||
          Utils.safe_get_array(level_solved, i-3) == Some(true)
         ) {
        Unlocked;
      } else {
        Locked;
      }
    }
  });


  // let title_info = (level.name == "madden") ?  {
  //     prefix: "Needs",
  //     damned: "Damned",
  //     suffix: "Massage",
  //   } : (level.name == "crypt") ? {
  //     prefix: "Send A",
  //     damned: "Dayum",
  //     suffix: "Message",
  //   } : (level.name == "meme") ? {
  //     prefix: "Send A",
  //     damned: "Danged",
  //     suffix: "Message",
  //   } : (level.name == "emend") ? {
  //     prefix: "Send A",
  //     damned: "Darned",
  //     suffix: "Message",
  //   } : {
  //     prefix: "Send A",
  //     damned: "Damned",
  //     suffix: "Message",
  //   };
  let title_info = {
    prefix: "Send A",
    damned: "Damned",
    suffix: "Message",
  };

  scroll_messages();

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
    {React.string(title_info.prefix ++ " ")}
    <span className="damnedmessage">
    {React.string(title_info.damned)}
    </span>
    {React.string(" " ++ title_info.suffix)}
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
    <div style={ReactDOMRe.Style.make(~flexGrow="1", ~paddingLeft="20px", ~overflow="hidden"
, ())}>
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
            <div className="messages_container" id="messages_container">
              {
                ReasonReact.array(Array.of_list(List.mapi((i: int, attempt: attempt) => {
                  <div className="message_pair" key={string_of_int(i)} >
                    <pre className="undamnedmessage"><span>
                      {React.string(attempt.message)}
                    </span></pre>
                    <br/>
                    <pre className={(attempt.damned === level.goal) ? "goodmessage" : "damnedmessage"}><span>
                      {React.string(attempt.damned)}
                    </span></pre>
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
                  <div style={ReactDOMRe.Style.make(~fontWeight="bold", ~marginBottom="10px", ())}>
                    <span className="unselectable">{React.string("Goal is to send: ")}</span>
                    <pre className="goodmessage">
                    <span>{React.string(level.goal)}</span>
                    </pre>
                  </div>
                  <form className="fullwidth" onSubmit={event => {
                    Js.log("sending message: " ++ state.message);
                    ReactEvent.Form.preventDefault(event);
                    dispatch(SendMessage);
                  }} autoComplete="off">
                    <div style={ReactDOMRe.Style.make(~paddingRight="10px", ())}>
                      <input id="main-input" className="fullwidth" type_="text" value={state.message}
                        onChange={event => dispatch(SetMessage(event->ReactEvent.Form.target##value))}
                        onKeyDown={event => dispatch(SetMessageCursor(event->ReactEvent.Keyboard.keyCode))} tabIndex={0}
                    >
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
