from tools import (
  gh, lm, eva, exe
)

def run(precision=7, par="../../"):
  '''
  Train and Test Ridge Regression
    on Boston Housing Data
  '''
  ...
  ###
  # Get Housing Data
  # for Training
  # and Testing
  ###
  (
    train,
    test
  ) = gh(par)
  ###
  # Set Alpha Values
  ###
  alphas = [
    0.1, 1,
    5, 50
  ]
  ###
  # Get Ridge Models
  # and Predictions
  ###
  (
    ridges,
    predicted
  ) = exe(
    lm.Ridge,
    train,
    test,
    alphas
  )
  ###
  # Select Evaluations
  ###
  selected = [
    "train", "test",
    "mse", "mae", "r2"
  ]
  ###
  # Evaluate Ridge Models
  ###
  eva(
    "RIDGE",
    ridges,
    train,
    test,
    predicted,
    precision,
    selected,
    alphas
  )
  
if __name__ == "__main__":
  ...
  run()
  