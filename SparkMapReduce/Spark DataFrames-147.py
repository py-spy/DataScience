## 1. The Spark DataFrame: An Introduction ##

f = open('census_2010.json')

for i in range(0,4):
    print(f.readline())

## 3. Schema ##

sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.printSchema()

## 4. Pandas vs Spark DataFrames ##

df.show(5)

## 5. Row Objects ##

first_five = df.head(5)
for item in first_five:
    print(item.age)

## 6. Selecting Columns ##

#df[['age']].show()
#df[['males']].show()
#df[['females']].show()
(df.select('age', 'males', 'females')).show()


## 7. Filtering Rows ##

fifty_plus = df[df['age']>5]
fifty_plus.show()

## 8. Using Column Comparisons as Filters ##

df[df['females'] < df['males']].show()

## 9. Converting Spark DataFrames to pandas DataFrames ##

pandas_df = df.toPandas()
import matplotlib.pyplot as plt
plt.hist(pandas_df['total'])
plt.show()