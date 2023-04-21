import pandas as pd
import numpy as np

def load(dataset):
  if len(dataset) == 100000:
    return 1
  else:
    print("Original loaded dataset has incorrect number of entries. Did you load the right file?")
    return 0

def filter(filtered_dataset):
  if len(filtered_dataset) == 84346:
    return 1
  else:
    print("Incorrect number of entries after filtering. Did you filter out all patients with HbA1c < 8?")
    return 0

def frac_drugA(fraction_drugA):
  if round(fraction_drugA, 3) == 0.633:
    return 1
  else:
    print("Incorrect fraction of patients who received drug A. Did you round the result? Did you report the result as a decimal?")
    return 0

def mean_a1c_change(mean_drugA_a1c_change):
  if round(mean_drugA_a1c_change, 3) == -1.188:
    return 1
  else:
    print("Incorrect mean A1c change in patients who received drug A. Did you exclude patients who received placebo?")
    return 0

def t_test(t_test_p_value):
  if round(t_test_p_value, 3) == 0:
    return 1
  else:
    print("Incorrect t-test p value. Did you compare patients who received drug A to those who received placebo?")

def a1c_below8(filtered_dataset):
  if (filtered_dataset['FinalA1c_Below8'].dtype == 'int64') and (round(filtered_dataset['FinalA1c_Below8'].mean(), 3) == 0.34):
    return 1
  else:
    print("FinalA1c_Below8 incorrectly calculated. Did you convert to an integer (0 or 1)?")
    return 0

def odds_ratio(or_):
  if round(or_, 3) == 7.324:
    return 1
  else:
    print("Odds ratio computed incorrectly.")
    return 0

def adjusted_odds_ratio_drugA(aor_drugA):
  if round(aor_drugA, 2) == 7.67:
    return 1
  else: 
    print("Adjusted odds ratio computed incorrectly. Did you include Exercise as a covariate?")
    return 0

def adjusted_odds_ratio_exercise(aor_exercise):
  if round(aor_exercise, 2) == 2.29:
    return 1
  else: 
    print("Adjusted odds ratio for Exercise computed incorrectly.")
    return 0

def chi_squared(chi2_p_value):
  if round(chi2_p_value, 3) == 0.157:
    return 1
  else:
    print("Incorrect chi-squared p value. Did you compare rates of hypoglycemia between patients who received drug A vs. placebo?")
    return 0