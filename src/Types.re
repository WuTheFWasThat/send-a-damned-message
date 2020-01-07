type level = {
  name: string,
  fn: string => string,
  goal: string,
  answer: string,
};

type savestate = {
  solved: Js.Dict.t(string),
  level: int
}
