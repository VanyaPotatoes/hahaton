import os
import matplotlib.pyplot as plt
import seaborn as sns
from unittest import skip
import numpy as np
import pandas as pd 
import requests
from bs4 import BeautifulSoup as bs


regions=[]
region_codes=[]
URL_TEMPLATE = "https://calcus.ru/kody-regionov"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")
region_names = soup.find_all('td')
counter=0
for i in region_names[2:]:
    i = i.text
    if counter%2==0:#проверка на то что номер региона
        if i.__contains__(","):#проверка на то, что номеров несколько
            i=i.split(",")[0]
            region_codes.append(i)
        else:
            region_codes.append(i)
    else:
        regions.append(i)
    counter = counter+1

dict_of_regions = {regions[i]: region_codes[i] for i in range(len(regions))} 

def transform_region(reg):
    for key, value in dict_of_regions.items():
        if reg=="г Санкт-Петербург":
            return 78
        if reg=="г Москва":
            return 77
        if reg.__contains__(key):
            return value

pd.set_option('display.max_rows', None)
train_data = pd.read_csv("C:\\Users\\Администратор\\Desktop\\1hackathon.csv")
print(train_data["region"].value_counts())

train_data["region"] = train_data["region"].map(transform_region)

print(train_data["region"].value_counts())

train_data.to_csv("C:\\Users\\Администратор\\Desktop\\prepared_data.csv")
