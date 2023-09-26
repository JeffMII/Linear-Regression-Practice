from tools import (
  gh, lm, eva, exe
)

def run(precision=7, par="../../"):
  '''
  Train and Test Logistic Regression
    on Boston Housing Data
  '''
  ...
  ###
  # Get Adult Data
  # for Training
  # and Testing
  ###
  (
    train,
    test
  ) = gh(par)
  ###
  # Get Linear Model
  # and Predictions
  ###
  (
    linear,
    predicted
  ) = exe(
    lm.LinearRegression,
    train, test
  )
  ###
  # Select Evaluations
  ###
  selected = [
    "train", "test", 
    "mse", "mae", "r2"
  ]
  ###
  # Evaluate Linear Model
  ###
  eva(
    "LINEAR",
    linear,
    train,
    test,
    predicted,
    precision,
    selected,
  )

if __name__ == "__main__":
  ...
  run()
