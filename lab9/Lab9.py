#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Answer 1
'''
The problem assgined in lab 9 is supervised machine learning problem where features are defined in dataset.
'''

# Answer 2

'''
The main difference between regression and classification is that
in regression the output is numerical/continuous while that for classification is categorical/discrete.

Our major goal is to diagnose the cancer, so it is clearly a classification problem.

'''


# In[18]:


# Answer 3

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

dataset = datasets.load_breast_cancer()
X = dataset.data #features
y = dataset.target #target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# part a using SGD classifier
model = SGDClassifier()
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)
print ("The accuracy using SGD classifier is ", metrics.accuracy_score(y_test, y_test_pred))


# part a using Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)
print ("The accuracy using Decision Tree Classifier is ", metrics.accuracy_score(y_test, y_test_pred))

# part a using Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)
print ("The accuracy using Random Forest Classifier is ", metrics.accuracy_score(y_test, y_test_pred))


# In[23]:


# Answer 4

from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

iris = datasets.load_breast_cancer()
X = iris.data
y = iris.target
X = scale(X)
X= PCA(n_components=5).fit_transform(X) #PCA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# part a using SGD classifier
model = SGDClassifier()
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)
print ("The accuracy using SGD classifier and PCA is ", metrics.accuracy_score(y_test, y_test_pred))


# part a using Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)
print ("The accuracy using Decision Tree Classifier and PCA is ", metrics.accuracy_score(y_test, y_test_pred))

# part a using Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)
print ("The accuracy using Random Forest Classifier and PCA is ", metrics.accuracy_score(y_test, y_test_pred))


# In[36]:


# Answer 5

'''
I am selecting random forest classifier as a favourite model and the confusion matrix is developed
'''

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import numpy as np

dataset = datasets.load_breast_cancer()
X = dataset.data #features
y = dataset.target #target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# part a using SGD classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_test_pred)
print("Confusion matrix is ",cm)
accuracy_of_confusion_matrix = (cm[0,0]+cm[1,1])/np.sum(cm)
print("Accuracy of confusion matrix is ",accuracy_of_confusion_matrix)
''' The model is highly effective as accuracy through confusion matrix is almost 95%'''

'''
for cancer diagnosis a given patient have disease X or not. 
It is better to have false positives here which can assert that a patient has a disease,
and then later realize that the decision was wrong, maybe after more tests / some preliminary medication. 
However, a false negative here means that someone who had a disease was not provided proper medical treatment,
which could be fatal.'''


# In[ ]:




