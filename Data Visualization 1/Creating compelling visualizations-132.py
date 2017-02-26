## 3. Seaborn styling ##

import seaborn as sns
births['agepreg'].hist()
sns.plt.show()

## 6. Practice: customizing distplot() ##

sns.set_style('dark')
sns.distplot(births['birthord'], kde=False, axlabel='Birth number')
sns.plt.show()

## 7. Boxplots: boxplot() ##

sns.set_style('dark')
births = pd.read_csv('births.csv')
sns.boxplot(x='birthord', y='agepreg', data=births)
sns.plt.show()

## 8. Pair plot: pairplot() ##

births = pd.read_csv('births.csv')
sns.set_style('dark')
sns.pairplot(births[['agepreg','prglngth','birthord']])
sns.plt.show()