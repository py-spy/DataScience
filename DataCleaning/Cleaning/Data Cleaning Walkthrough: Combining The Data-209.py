## 2. Condensing class size ##

class_size = data["class_size"]
class_size = class_size[class_size["GRADE "] == "09-12"]
class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"]
print(class_size.head())

## 3. Computing average class sizes ##

import numpy
class_size = class_size.groupby("DBN").agg(numpy.mean)
class_size.reset_index(inplace=True)
data["class_size"] = class_size
print(data["class_size"].head())

## 4. Condensing demographics ##

data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]
print(data["demographics"].head())

## 5. Condensing graduation ##

data['graduation'] = data['graduation'][data['graduation']['Cohort']=='2006']
data['graduation'] = data['graduation'][data['graduation']['Demographic']=='Total Cohort']
print(data['graduation'].head())

## 6. Converting AP test scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for col in cols:
    data["ap_2010"][col] = pd.to_numeric(data["ap_2010"][col], errors="coerce")
    
print(data["ap_2010"].head())

## 8. Performing the left joins ##

combined = data["sat_results"]
combined = combined.merge(data["ap_2010"], on="DBN", how="left")
combined = combined.merge(data["graduation"], on="DBN", how="left")
print(combined.head(5))
print(combined.shape)

## 9. Performing the inner joins ##

to_merge = ["class_size", "demographics", "survey", "hs_directory"]

for m in to_merge:
    combined = combined.merge(data[m], on="DBN", how="inner")

print(combined.head(5))
print(combined.shape)

## 10. Filling in missing values ##

combined = combined.fillna(combined.mean())
combined = combined.fillna(0)

print(combined.head(5))

## 11. Adding a school district column ##

def get_first_two_chars(dbn):
    return dbn[0:2]

combined["school_dist"] = combined["DBN"].apply(get_first_two_chars)
print(combined["school_dist"].head())