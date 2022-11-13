import os
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from unittest import skip
import numpy as np
import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

train_data = pd.read_csv("C:\\Users\\Администратор\\Desktop\\okved1.csv")
km=KMeans(n_clusters=5)
y_predicted = km.fit_predict(train_data[['okved','registration_date']])
scaler = MinMaxScaler()
scale = scaler.fit_transform(train_data[['okved','registration_date']])
train_data = pd.DataFrame(scale, columns = ['okved','registration_date']);
train_data['Clusters'] = km.labels_
sns.scatterplot(x="registration_date", y="okved",hue = 'Clusters',  data=train_data, alpha=0.05)

train_data.to_csv("C:\\Users\\Администратор\\Desktop\\predicted_data.csv")
#output the plot
