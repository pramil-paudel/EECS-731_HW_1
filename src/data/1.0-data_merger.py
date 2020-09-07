# %%
# %%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

print("Packages Loaded")

PROJECT_ROOT_DORECTORY = '~/Documents/FALL_2020/INTRO_DATASCIENCE/WEEKLY_PROJECT/week_one'

us_confirmed_case = pd.read_csv(PROJECT_ROOT_DORECTORY + "/data/raw/time_series_covid_19_confirmed_US.csv")
us_confirmed_case.head(10)

us_confirmed_death = pd.read_csv(PROJECT_ROOT_DORECTORY + "/data/raw/time_series_covid_19_deaths_US.csv")
us_confirmed_death.head(10)

us_confirmed_case_trimmed = us_confirmed_case.drop(us_confirmed_case.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]])
us_confirmed_case_trimmed.head(10)
