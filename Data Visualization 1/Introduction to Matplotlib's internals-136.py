## 2. Levels of abstraction ##

import matplotlib.pyplot as plt

# 2 simple lists of values
month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]
plt.scatter(month, temperature)
plt.show()

## 5. Axes ##

import numpy as np
month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([0,14])
plt.show()

## 7. Customizing the plot ##

import numpy as np

month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([np.min(month),np.max(month)])
ax.set_ylim([np.min(temperature), np.max(temperature)])

color = 'darkblue'
marker = 'o'

# run the .scatter() method, params: color, marker
ax.scatter(month, temperature, color='darkblue', marker='o')
plt.show()

## 8. Setting multiple attributes easily ##

month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set(xlim=(0,13), ylim=(10,110))
ax.scatter(month, temperature, color='darkblue', marker='o') #add xlabel, ylabel, and title
plt.show()

## 10. Adding data to multiple subplots ##

month_2013 = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature_2013 = [32,18,40,40,50,45,52,70,85,60,57,45]
month_2014 = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature_2014 = [35,28,35,30,40,55,50,71,75,70,67,49]