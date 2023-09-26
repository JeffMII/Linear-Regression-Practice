from pandas import (
  read_csv as csv,
  concat as cat,
  DataFrame as DF,
  Categorical as C
)
from typing import (
  Callable as Call,
  Iterable as Iter,
  TypeAlias as Alias,
  Union as Union
)
from functools import (
  partial as part
)
from sklearn import (
  linear_model as lm
)
from .core import (
  LinearModel as LM,
  mapart as mprt
)
from sklearn.model_selection import (
  train_test_split as tts
)
from sklearn.metrics import (
  mean_squared_error as mse,
  mean_absolute_error as mae,
  accuracy_score as acc,
  r2_score as r2,
)
from .data import (
  getHousing as gh,
  getAdult as ga
)
from .score import (
  evaluate as eva
)
from .model import (
  execute as exe
)
__all__: tuple = (
  "csv", "lm", "cmp",
  "tts", "mse", "mae",
  "acc", "r2", "part",
  "gh", "LM", "eva",
  "exe", "cat", "ga",
  "arr", "DF", "C",
  "Call", "Iter", "hdr",
  "mprt" "LM", "Alias"
)
