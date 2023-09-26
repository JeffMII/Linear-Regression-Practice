from tools import (
  lm, Alias, Union,
  Call, Iter, part
)

LinearModel: Alias = Union[
  lm.LinearRegression,
  lm.Ridge, lm.Lasso,
  lm.LogisticRegression
]

def mapart(
  fn: Call[..., str | int | float], *args,
  its: Iter[Iter], **kwargs
) -> list[str | int | float]:
  ...
  return list(map(part(
    fn, *args,
    **kwargs
  ), its))
  