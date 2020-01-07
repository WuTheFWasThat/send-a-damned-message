let reasonReactBlue = "#48a9dc";
let lightgray = "rgb(222, 222, 222)";
let darkgray = "rgb(111, 111, 111)";
// let selected_color = "rgb(222, 222, 111)";
let good_color = "rgb(64, 222, 64)";

// The {j|...|j} feature is just string interpolation, from
// bucklescript.github.io/docs/en/interop-cheatsheet#string-unicode-interpolation
// This allows us to conveniently write CSS, together with variables, by
// constructing a string
let style = {j|
  body {
    background-color: $darkgray;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px 40px;
  }
  .center {
    text-align: center;
    align-items: center;
  }
  .react-main {
    width: 100%;
  }
  .fullwidth {
    width: 100%;
  }
  .levelselect {
    width: 100px;
  }
  .levelselect .levelitem {
    border: 1px solid $darkgray;
    background-color: $lightgray;
    border-radius: 10px;
    text-align: center;
    padding: 5px;
  }
  .selectedlevel.levelitem {
    border-width: 3px !important;
  }
  .levelitem.beaten {
    background-color: $good_color !important;
  }
  button {
    background-color: white;
    color: $reasonReactBlue;
    box-shadow: 0 0 0 1px $reasonReactBlue;
    border: none;
    padding: 8px;
    font-size: 16px;
  }
  button:active {
    background-color: $reasonReactBlue;
    color: white;
  }
  .container {
    margin: 12px 0px;
    box-shadow: 0px 4px 16px rgb(200, 200, 200);
    border-radius: 12px;
    font-family: sans-serif;
  }
  .containerTitle {
    text-align: center;
    background-color: rgb(242, 243, 245);
    border-radius: 12px 12px 0px 0px;
    padding: 12px;
    font-weight: bold;
    font-size: 24px;
  }
  .containerContent {
    background-color: white;
    padding: 16px;
    border-radius: 0px 0px 12px 12px;
  }
  .damnedmessage {
    // background-color: rgb(256, 224, 224);
    color: rgb(256, 128, 128);
    display: inline-block;
  }
  .goodmessage {
    color: $good_color;
    // color: rgb(256, 64, 64);
    display: inline-block;
  }
  .undamnedmessage {
    // background-color: rgb(256, 256, 224);
    display: inline-block;
  }
|j};
