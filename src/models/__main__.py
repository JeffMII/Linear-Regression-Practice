import linear
import ridge
import lasso
import logistic

if __name__ == "__main__":
  ...
  ###
  # Set Precision
  ###
  precision, par = (
    7, "../"
  )
  ###
  # Run All Models
  ###
  linear.run(
    precision, par
  )
  ridge.run(
    precision, par
  )
  lasso.run(
    precision, par
  )
  logistic.run(
    precision, par
  )