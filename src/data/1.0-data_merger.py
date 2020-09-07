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

# Replacing day wise data with 1 value if no case is cofirmed to handle NaN case
us_confirmed_case_day_wise_data = us_confirmed_case.drop(
    us_confirmed_case.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 1).replace(0, 1)

us_confirmed_death_day_wise_data = us_confirmed_death.drop(
    us_confirmed_death.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 1)

us_confirmed_death_day_wise_percentage = pd.DataFrame(
    us_confirmed_death_day_wise_data / us_confirmed_case_day_wise_data).round(3)

print(us_confirmed_death_day_wise_percentage.head(10))
# Creating new DF with % value
us_confirmed_death_other_data = us_confirmed_death[
    ["UID", "iso2", "iso3", "code3", "FIPS", "Admin2", "Province_State", "Country_Region", "Lat", "Long_",
     "Combined_Key"]]

# Creating a new % data frame
merged_df = pd.concat([us_confirmed_death_other_data, us_confirmed_death_day_wise_percentage], axis=1)
merged_df.to_csv(PROJECT_ROOT_DORECTORY + "/data/processed/time_series_covid_19_deaths_US_percentage.csv")
