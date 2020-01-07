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
  attempts: list(attempt),
  savestate: Types.savestate,
};

type action =
  SendMessage
  | SetMessage(string);

[@react.component]
let make = (~levels: array(Types.level), ~savestate: Types.savestate) => {
  let reducer = (state, action) => {
    switch (action) {
      | SetMessage(msg) => { ...state, message: msg }
      | SendMessage => {
        let message = state.message;
        let level = levels[state.savestate.level];
        let damned_message = level.fn(message);
        let attempt = {
          message: message, damned: damned_message
        };
        {
          ...state,
          attempts: List.concat([state.attempts, [attempt]]), message: ""
        };
      }
    };
  };
  let initialState = { message: "", attempts: [], savestate: savestate, };

  let (state, dispatch) = React.useReducer(reducer, initialState);
  let level = levels[state.savestate.level];


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
    <div>
      <div>
        {React.string("Goal is to send ")}
        <span className="goodmessage">
        {React.string(level.goal)}
        </span>
      </div>
      <ul>
        {
          ReasonReact.array(Array.of_list(List.mapi((i: int, attempt: attempt) => {
            <div key={string_of_int(i)}>
              <div>
                <span className="undamnedmessage">
                  {React.string(attempt.message)}
                </span>
              </div>
              <div>
                <span className={(attempt.damned === level.goal) ? "goodmessage" : "damnedmessage"}>
                  {React.string(attempt.damned)}
                </span>
              </div>
            </div>
          }, state.attempts)))
        }
      </ul>
      <form onSubmit={event => {
        Js.log("sending message: " ++ state.message);
        ReactEvent.Form.preventDefault(event);
        dispatch(SendMessage);
      }}>
      <input type_="text" value={state.message} onChange={event => dispatch(SetMessage(event->ReactEvent.Form.target##value))}>
      </input>
      </form>
    </div>
    </div>
    </div>
  </div>;
};
