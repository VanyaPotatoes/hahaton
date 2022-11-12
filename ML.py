import os
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from unittest import skip
import numpy as np
import pandas as pd 

train_data = pd.read_csv("C:\\Users\\Администратор\\Desktop\\ready.csv")
sns.histplot(data=train_data["region"])
#Output plot on Jupiter Notebook
train_data = train_data.drop("Unnamed: 0", axis=1)
train_data.dropna(subset="region")
df= train_data.drop(index=train_data.index[1:3653500])
df.shape
#(507, 6)
km=KMeans(n_clusters=5)
y_predicted = km.fit_predict(df[['okved','region']])
y_predicted
km.cluster_centers_
""" 
array([[46.01324503, 47.09271523],
       [45.53157895, 72.6       ],
       [80.5106383 , 67.31914894],
       [43.23333333, 16.62222222],
       [86.03448276, 26.03448276]])
"""
df['Clusters'] = km.labels_
sns.scatterplot(x="okved", y="region",hue = 'Clusters',  data=df,palette='viridis')
