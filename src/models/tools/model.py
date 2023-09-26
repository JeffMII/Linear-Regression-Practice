from tools import (
  mprt, LM
)

def _fit(model: LM, *, x, y):
  ...
  return model.fit(x, y)

def _predict(model: LM, *, x):
  ...
  return model.predict(x)

def execute(
  cls: type[LM],
  train, test,
  alphas: list=None,
  *args,
  **kwargs
) -> list[LM, list]:
  '''
  Fits and Predicts Models
    with or without Alpha Values
  '''
  ...
  ###
  # Initialize Models
  ## with Alpha Values
  ## if alphas not None
  ###
  models = mprt(
    cls, *args,
    its=alphas,
    **kwargs
  ) if alphas else [
    cls(*args, **kwargs)
  ]
  ###
  # Fit Models
  ###
  models = mprt(
    _fit,
    x=train["x"],
    y=train["y"],
    its=models
  )
  ###
  # Predict
  ###
  predicted = mprt(
    _predict,
    x=test["x"],
    its=models
  )
  ###
  # Return Models and Predictions
  ###
  return models, predicted