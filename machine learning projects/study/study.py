# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 21:43:07 2019

@author: Rohit_V03
"""

from sklearn.preprocessing import MinMaxScaler
import numpy

weights = numpy.array([[115.],[140.],[175.]])
scaler  = MinMaxScaler()
rescaled_weights = scaler.fit_transform(weights)
print(rescaled_weights)