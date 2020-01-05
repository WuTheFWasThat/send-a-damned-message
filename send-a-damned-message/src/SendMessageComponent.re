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
  attempts: list(attempt)
};

type action =
  SendMessage
  | SetMessage(string);

let initialState = {message: "", attempts: []};

let reducer = (state, action) => {
  switch (action) {
    | SetMessage(msg) => { ...state, message: msg }
    | SendMessage => {
      let message = state.message;
      let damned_message = message;
      let attempt = {
        message: message, damned: damned_message
      };
      {attempts: List.concat([state.attempts, [attempt]]), message: ""};
    }
  };
};

[@react.component]
let make = () => {
  let (state, dispatch) = React.useReducer(reducer, initialState);

  <div
    style={ReactDOMRe.Style.make(~display="flex", ~alignItems="center", ~justifyContent="space-between", ())}>
    <div>
      <ul>
        {
          ReasonReact.array(Array.of_list(List.mapi((i: int, attempt: attempt) => {
            <div key={string_of_int(i)}>
              <div>
                {React.string(attempt.message)}
              </div>
              <div>
                {React.string(attempt.damned)}
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
  </div>;
};
