## 1. Data Structures ##

import pandas as pd
fandango = pd.read_csv("fandango_score_comparison.csv")
fandango.head()

## 2. Integer Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango["FILM"]
series_rt = fandango["RottenTomatoes"]

## 3. Custom Indexes ##

# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values
series_custom = Series(rt_scores, index = film_names)

## 4. Integer Index Preservation ##

series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]
fiveten = series_custom.iloc[5:10]
print(fiveten)

## 5. Reindexing ##

original_index = series_custom.index.tolist()
x = sorted(original_index)
sorted_by_index = series_custom.reindex(x)

## 6. Sorting ##

sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
print(sc2[0:10], sc3[0:10])

## 7. Transforming Columns With Vectorized Operations ##

series_normalized = series_custom/20

## 8. Comparing and Filtering ##

criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[(series_custom > 50) & (series_custom < 75)]

## 9. Alignment ##

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_critics+rt_users)/2
print(rt_mean)