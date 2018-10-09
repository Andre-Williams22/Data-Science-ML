#!/usr/bin/env python
# coding: utf-8

# In[17]:


import sys
import numpy 
import pandas
import matplotlib
import seaborn
import scipy
import sklearn
print('Python: {}'.format(sys.version))
print('Numpy: {}'.format(numpy.__version__))
print('Pandas: {}'.format(pandas.__version__))
print('Matplotlib: {}'.format(matplotlib.__version__))
print('Seaborn: {}'.format(seaborn.__version__))
print('Scipy: {}'.format(scipy.__version__))
print('Sklearn: {}'.format(sklearn.__version__))


# In[18]:


# import the necessary packages 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt # for graphical interface
import seaborn as sns


# In[19]:


# Load the dataset from the csv file using pandas
data = pd.read_csv('creditcard.csv')


# In[20]:


# Time to explore the dataset
print(data.columns)


# In[21]:


# lets figure out the shape of the data
print(data.shape)


# In[22]:


data = data.sample(frac=0.1, random_state = 1)
print(data.shape)
print(data.describe()) #this gives us useful information about each column
# V1 - V28 are the results of a PCA Dimensionality reduction to protect user identities and sensitive features


# In[23]:


#This is a much more reasonable size of data to work with. 
# We have imported the csv file, we've looked at each of the columns and the column names and the distributions. Another way to do that is to plot a histogram of the data.
data.hist(figsize = (20, 20))
plt.show()


# In[24]:


# Lets actually calculate the number of fradulate cases we actually have and valid cases so we can get an outlier fraction to go into our anomaly detection algorithm.
Fraud = data[data['Class'] == 1]
Valid = data[data['Class'] == 0]

outlier_fraction = len(Fraud) / float(len(Valid))
print(outlier_fraction)
                                      
                                      
print('Fraud Cases: {}'.format(len(data[data['Class'] == 1])))
print('Valid Transactions: {}'.format(len(data[data['Class'] == 0]))) 


# In[25]:


# Correlation Matrix
corrmat = data.corr()
fig = plt.figure(figsize = (12, 9))

sns.heatmap(corrmat, vmax = .8, square = True)
plt.show()


# In[26]:


# The lighter ones are stronger positive correlation
# Get all the columns from the DataFrame

columns = data.columns.tolist()

# Filter the columns to remove data we do not want
columns = [c for c in columns if c not in ["Class"]]

# This is unsupervised learning since this is anamoly detection so we dont want the labels to be sent to our networks ahead of time.

target = "Class"

X = data[columns]
Y = data[target]

# Print shapes
print(X.shape)
print(Y.shape)


# In[26]:


# Applying the Algorithms 


# In[44]:


from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

# define a random state
state = 1

classifiers = {
    "Isolation Forest": IsolationForest(max_samples=len(X),
                                       contamination=outlier_fraction,
                                       random_state=state),
     "Local Outlier Factor": LocalOutlierFactor(
     n_neighbors = 20,
     contamination = outlier_fraction)
}

import pickle
# fit the model
plt.figure(figsize=(9, 7))
n_outliers = len(Fraud)


for i, (clf_name, clf) in enumerate(classifiers.items()):
    
    # fit the data and tag outliers
    if clf_name == "Local Outlier Factor":
        y_pred = clf.fit_predict(X)
        scores_pred = clf.negative_outlier_factor_
    else:
        clf.fit(X)
        scores_pred = clf.decision_function(X)
        y_pred = clf.predict(X)
    
    # Reshape the prediction values to 0 for valid, 1 for fraud. 
    y_pred[y_pred == 1] = 0
    y_pred[y_pred == -1] = 1
    
    n_errors = (y_pred != Y).sum()
    
    # Run classification metrics
    print('{}: {}'.format(clf_name, n_errors))
    print(accuracy_score(Y, y_pred))
    print(classification_report(Y, y_pred))


# In[ ]:




