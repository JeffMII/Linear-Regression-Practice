from tools import (
  lm, ga, exe, eva
)

def run(precision=7, par="../../"):
  '''
  Train and Test Logistic Regression
    on Combined Adult Data
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
  ) = ga(par)
  ###
  # Get Logistic Model
  # and Predictions
  ###
  (
    logistic,
    predicted
  ) = exe(
    lm.LogisticRegression,
    train, test,
    max_iter=300
  )
  ###
  # Select Evaluations
  ###
  selected = [
    "train", "test",
    "accuracy"
  ]
  ###
  # Evaluate Logistic Model
  ###
  eva(
    "LOGISTIC",
    logistic,
    train,
    test,
    predicted,
    precision,
    selected
  )
  
if __name__ == "__main__":
  ...
  run()
