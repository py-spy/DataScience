## 2. Holdout validation ##

import numpy as np
np.random.seed(8)
admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)
rand_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[rand_index]
train = shuffled_admissions.iloc[0:515]
test = shuffled_admissions.iloc[515: len(admissions)]
print(shuffled_admissions[0:5])

## 3. Accuracy ##

import numpy as np
np.random.seed(8)

shuffled_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[shuffled_index]
train = shuffled_admissions.iloc[0:515]
test = shuffled_admissions.iloc[515:len(shuffled_admissions)]
lr = LogisticRegression()
lr.fit(train[['gpa']], train['actual_label'])
test['predicted_label'] = lr.predict(test[['gpa']])
accuracy = len(test[test['actual_label']==test['predicted_label']])/(len(test))
print(accuracy)

## 4. Sensitivity and specificity ##

model = LogisticRegression()
model.fit(train[["gpa"]], train["actual_label"])
labels = model.predict(test[["gpa"]])
test["predicted_label"] = labels
matches = test["predicted_label"] == test["actual_label"]
correct_predictions = test[matches]
accuracy = len(correct_predictions) / len(test)
true_positive = len(test[(test['actual_label'] == 1) & (test['predicted_label'] ==1)])
false_negative = len(test[(test['actual_label']==1) & (test['predicted_label'] ==0)])
false_positive = len(test[(test['actual_label']==0) & (test['predicted_label'] ==1)])
true_negative = len(test[(test['actual_label']==0) & (test['predicted_label'] ==0)])
sensitivity = true_positive / (true_positive + false_negative)
specificity = true_negative / (false_positive + true_negative)
print(sensitivity, specificity)

## 6. ROC curve ##

import matplotlib.pyplot as plt
from sklearn import metrics
probabilities = lr.predict_proba(test[['gpa']])
fpr,tpr,threshholds = metrics.roc_curve(test['actual_label'], probabilities[:,1])
plt.plot(fpr,tpr)

## 7. Area under the curve ##

# Note the different import style!
from sklearn.metrics import roc_auc_score
probabilities = lr.predict_proba(test[['gpa']])
auc_score = roc_auc_score(test['actual_label'], probabilities[:,1])
print(auc_score)