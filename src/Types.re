type level = {
  name: string,
  fn: string => string,
  goal: string,
  answer: string,
};

type savestate = {
  // mapping from levels to solutions
  answers: Js.Dict.t(string),
  level: int
}
