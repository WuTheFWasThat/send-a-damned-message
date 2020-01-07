type level = {
  name: string,
  fn: string => string,
  goal: string,
};
type savestate = {
  solved: Js.Dict.t(string),
  level: int
}
