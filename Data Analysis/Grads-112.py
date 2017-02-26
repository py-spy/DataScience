## 2. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages[0:5], recent_grads[0:5])

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()
def cal_total(df):
    cat = df["Major_category"].unique()
    count_dict = {}
    for item in cat:
        major_df = df[df["Major_category"] == item]
        total = major_df["Total"].sum()
        count_dict[item] = total
    return count_dict
aa_cat_counts = cal_total(all_ages)
rg_cat_counts = cal_total(recent_grads)

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0
x = recent_grads["Low_wage_jobs"].sum()
y = recent_grads["Total"].sum()
low_wage_percent = float(x/y)
print(low_wage_percent)

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0
for m in majors:
    recent_grads_row = recent_grads[recent_grads['Major'] == m]
    all_ages_row = all_ages[all_ages['Major'] == m]
    
    rg_unemp_rate = recent_grads_row.iloc[0]['Unemployment_rate']
    aa_unemp_rate = all_ages_row.iloc[0]['Unemployment_rate']
    
    if rg_unemp_rate < aa_unemp_rate:
        rg_lower_count += 1

print(rg_lower_count)