from tools import (
  csv, tts, cat, DF, C
)

def getHousing(par=""):
  '''
  Get and Split Boston Housing Data
    for Training and Testing
  '''
  ...
  ###
  # Set Directory
  ###
  par += 'resources/housing/'
  ###
  # Get Housing Data
  ###
  data = csv(
    f'{par}housing.csv',
    delimiter=',',
    header=None
  ).values
  ###
  # Set Data Containers
  # for Training
  # and Testing
  ###
  train, test = ({
    "x": [], "y": []
  }, {
    "x": [], "y": []
  })
  ###
  # Split Data
  ###
  (
    train["x"], test["x"],
    train["y"], test["y"]
  ) = tts(
    data[:, :-1], data[:, -1],
    train_size=0.80
  )
  ###
  # Return Data
  ###
  return train, test

def getAdult(par=""):
  '''
  Get, Combine, and Split Adult Data
    for Training and Testing
  '''
  ...
  ###
  # Set Directory
  ###
  par += 'resources/adult/'
  ###
  # Get and Combine Adult Data
  ###
  data = cat((
    csv(
      f'{par}adult.data.csv',
      delimiter='\s+',
      header=None
    ),
    csv(
      f'{par}adult.test.csv',
      delimiter='\s+',
      header=None
    )
  ))
  ###
  # Convert Non-Numeric Categories
  # to Numeric Categories
  ###
  data = DF({
    key: C(
      data[key]
    ).codes if (
      data[key].dtypes
      in ["object", "string"]
    ) else data[key]
    for key in data.columns
  }).values
  ###
  # Set Data Containers
  # for Training
  # and Testing
  ###
  train, test = {
    "x": [], "y": []
  }, {
    "x": [], "y": []
  }
  ###
  # Split Data
  ###
  (
    train["x"], test["x"],
    train["y"], test["y"]
  ) = tts(
    data[:, :-1],
    data[:, -1],
    train_size=0.80
  )
  ###
  # Return Data
  ###
  return train, test
