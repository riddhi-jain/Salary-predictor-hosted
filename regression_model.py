# -*- coding: utf-8 -*-
"""Linear Regression 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Il21ptFymIJ-_EcwkVvRHFwmkkauBb0x
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv("salary_predict_dataset.csv")
df.head()

df.isnull().sum()

df.info()

# filling null values of test_score column
df['test_score'].fillna(df['test_score'].mean(), inplace = True)
df.isnull().sum()

# filling null values of interview column
df['interview_score'].fillna(df['interview_score'].mean(), inplace = True)
# filling null values of experience column
df['experience'].fillna(0, inplace = True)
df.isnull().sum()

"""Now all missing values are filled. 

Now we need to convert string adta to numerical adta
"""

df['experience']

def string_to_num(word):
  dict = {'one':1, 'two':2, 'three':3, 'four':4,
          'five':5, 'six':6, 'seven':7, 'ten':10,
          'eleven':11, 'twelve':12, 'thirteen':13,
          'fifteen':15, 0:0}
  return dict[word]

df['experience'] = df['experience'].apply(lambda x : string_to_num(x))
df.info()

"""Now the object type experience is converted to integer"""

# defining feature and labels
x = df.iloc[:,:3]
y = df.iloc[:, -1]

# splitting data into traina and test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# importing algorithm and fitting the model
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train, y_train)

# saving the model
import pickle
pickle.dump(lr, open("model.pkl", "wb"))

# loading model to compare results
model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[2,8,5]]))