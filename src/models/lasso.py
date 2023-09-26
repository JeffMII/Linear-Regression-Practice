from tools import (
  lm, gh, eva, exe
)

def run(precision=7, par="../../"):
  '''
  Train and Test LASSO Regression
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
  # Set Aplpha Values
  ###
  alphas = [
    0.1, 1,
    5, 50
  ]
  ###
  # Get LASSO Models
  # and Predictions
  ###
  (
    lassos,
    predicted
  ) = exe(
    lm.Lasso,
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
  # Evaluate LASSO Models
  ###
  eva(
    "LASSO",
    lassos,
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