# Overview
This is a `Python` project that demonstrates the use of `Scikit-Learn` and `Pandas` libraries for linear regression and logistic regression tasks. The project involves reading data for four different linear regression models from Scikit-Learn, training the models using the loaded data, and evaluating their performance using various evaluation metrics.

# Dependencies

```
Python 3.x
Scikit-Learn
Pandas
```

# Installation

1. Clone the repository: 
   - `git clone https://github.com/JeffMII/LinearRegression-HW2.git`

2. Install the required dependencies: 
   - `pip install -r requirements.txt`

# Usage

## Load the data

For linear regression models (LinearRegression, Ridge, and LASSO), the project uses the Boston House Prices dataset from Scikit-Learn: 

> [Boston House Prices](https://www.kaggle.com/datasets/vikrishnan/boston-house-prices)

For the logistic regression model (LogisticRegression), the project uses the Adult financial classification dataset:

> [Adult](https://archive.ics.uci.edu/dataset/2/adult)

Be sure to place download the files to their respective directories and with the specific filenames:

- **Boston House Prices** (note that this file requires removing some spacing so that only commas are the delimiters):
  1. `HW2-LinearRegression/resources/housing/housing.csv`
- **Adult** (note that these two files require reformatting them to CSV with spaces as delimiters):
  1. `HW2-LinearRegression/resources/adult/adult.data.csv`
  2. `HW2-LinearRegression/resources/adult/adult.test.csv`

## Train, infer, and evaluate the models:

The project trains each of the four models using the loaded data. Then the trained models are used to make predictions on the test data.

### For a full run of the project, use the following command:

- Full Regression Run: `python HW2-LinearRegression/src/models`

### To run each model individually, use the following commands:

- Linear Regression: `python HW2-LinearRegression/src/models/linear.py`
- Ridge Regression: `python HW2-LinearRegression/src/models/ridge.py`
- LASSO Regression: `python HW2-LinearRegression/src/models/lasso.py`
- Logistic Regression: `python HW2-LinearRegression/src/models/logistic.py`

For linear regression models (LinearRegression, Ridge, and LASSO), the project evaluates the predictions using Mean Squared Error (MSE), Mean Absolute Error (MAE), and R^2 metrics. For the logistic regression model (LogisticRegression), the project evaluates the predictions using accuracy metric. The evaluation results are displayed tables, one for each model with their respective evaluation methods.

## Display results

```
#############################
#     LINEAR REGRESSION     #
#############################
# Training Scores | 0.75993 #
# Testing Scores  | 0.64141 #
# MSE Scores      | 39.1876 #
# MAE Scores      | 3.76714 #
# R2 Scores       | 0.64141 #
#############################

###########################################################
#                     RIDGE REGRESSION                    #
###########################################################
# Alpha Values    | 0.1     | 1       | 5       | 50      #
# Training Scores | 0.75297 | 0.75015 | 0.74367 | 0.73002 #
# Testing Scores  | 0.68162 | 0.68204 | 0.68112 | 0.68114 #
# MSE Scores      | 33.7161 | 33.6710 | 33.7683 | 33.7662 #
# MAE Scores      | 3.62607 | 3.56219 | 3.52887 | 3.60678 #
# R2 Scores       | 0.68162 | 0.68204 | 0.68112 | 0.68114 #
###########################################################

###########################################################
#                     LASSO REGRESSION                    #
###########################################################
# Alpha Values    | 0.1     | 1       | 5       | 50      #
# Training Scores | 0.71662 | 0.66023 | 0.56660 | 0.23243 #
# Testing Scores  | 0.75002 | 0.64581 | 0.51448 | 0.21813 #
# MSE Scores      | 23.8302 | 33.7646 | 46.2852 | 74.5363 #
# MAE Scores      | 3.54782 | 4.23912 | 4.96490 | 6.37382 #
# R2 Scores       | 0.75002 | 0.64581 | 0.51448 | 0.21813 #
###########################################################

#############################
#    LOGISTIC REGRESSION    #
#############################
# Training Scores | 0.80052 #
# Testing Scores  | 0.79885 #
# Accuracy Scores | 0.79885 #
#############################
```

# Contributing

Contributions are welcome! If you find any issues or want to enhance the project, feel free to open a pull request. This is mainly a project used to learn Scikit-Learn.

# License

This project is licensed under the MIT License.
