## 2. Introduction to the data ##

import pandas as pd
columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names = columns)
print(cars.head(5))

## 3. Exploratory data analysis ##

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
cars.plot("weight", "mpg", kind='scatter', ax=ax1)
cars.plot("acceleration", "mpg", kind='scatter', ax=ax2)
plt.show()

## 5. Scikit-learn ##

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(cars[['weight']], cars['mpg'])

## 6. Making predictions ##

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=True)
lr.fit(cars[["weight"]], cars["mpg"])
predictions = lr.predict(cars[['weight']])
predictions[0:5]

## 7. Plotting the model ##

import matplotlib.pyplot as plt
plt.scatter(cars['weight'], cars['mpg'], c='red')
plt.scatter(cars['weight'], predictions, c = 'blue')
plt.show()

## 8. Error metrics ##

from sklearn.metrics import mean_squared_error
lr = LinearRegression()
lr.fit(cars[["weight"]], cars["mpg"])
predictions = lr.predict(cars[["weight"]])
mse = mean_squared_error(cars['mpg'],predictions)
print(mse)

## 9. Root mean squared error ##

from math import sqrt
mse = mean_squared_error(cars["mpg"], predictions)
rmse = sqrt(mse)
print(rmse)