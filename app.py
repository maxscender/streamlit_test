import pandas as pd 
import streamlit as st 


df = pd.read_csv("sofascore.csv")

df['odd'] = pd.to_numeric(df['odd'])

def categorize_odd(value):
    if value < 1.5:
        return 'low'
    elif value < 2:
        return 'medium'
    else:
        return 'high'
df['odd_range'] = df['odd'].apply(categorize_odd)
st.dataframe(df)

