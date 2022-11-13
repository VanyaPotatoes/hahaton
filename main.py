import eel
import streamlit as st
import pandas as pd
df=pd.read_csv("C:\\Users\\HP\\Desktop\\hac\\web\\okved1.csv")
st.line_chart(df)
eel.init("C:\\Users\\HP\\Desktop\\hac\\web")
eel.start("Base.html", size=(1000,1500), mode="edge")