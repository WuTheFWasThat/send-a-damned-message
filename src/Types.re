type level = {
  name: string,
  fn: string => string,
  goal: string,
  answer: string,
};

type savestate = {
  // mapping from levels to solutions
  solved: Js.Dict.t(string),
  level: int
}
