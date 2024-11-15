import pandas as pd 
import streamlit as st 


df = pd.read_csv("sofascore.csv")

st.dataframe(df)
