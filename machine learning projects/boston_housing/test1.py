# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 14:53:29 2018

@author: Rohit_V03
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('housing.csv')
df.head(5)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop('MEDV', axis=1), df['MEDV'], test_size=0.3, random_state=101)



from sklearn.metrics import r2_score

def performance_metric(y_true, y_predict):
    """ Calculates and returns the performance score between 
        true and predicted values based on the metric chosen. """
    
    # TODO: Calculate the performance score between 'y_true' and 'y_predict'
    score = r2_score(y_true,y_predict)
    
    # Return the score
    #print("Model has a coefficient of determination, R^2, of {:.3f}.".format(score))
    return score


# Create cross-validation sets from the training data
cv_sets = ShuffleSplit(n_splits = 10, test_size = 0.20, random_state = 0)
print(cv_sets)
# TODO: Create a decision tree regressor object
regressor = DecisionTreeRegressor(random_state=0)
# TODO: Create a dictionary for the parameter 'max_depth' with a range from 1 to 10
dt_range = range(1, 11)
params = dict(max_depth=dt_range)
#print(params)
# TODO: Transform 'performance_metric' into a scoring function using 'make_scorer' 
scoring_fnc = make_scorer(performance_metric)
    
    
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(regressor, params, cv=cv_sets, scoring=scoring_fnc)

reg = grid.fit(X_train, y_train)

y_predict = reg.predict(X_test)
print(y_predict.coef_)