# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('C:/Users/abc/Desktop/ML models/trained_model.sav','rb'))

input = (8,183,64,0,0,23.3,0.672,32)

#converting input data as numpy array
input_as_numpy_array = np.asarray(input)

#reshaping input as we are prediciting for one instance only
input_reshaped = input_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_reshaped)

if (prediction[0] == 0):
  print("Person is non diabetic")
else:
  print("Person is diabetic")