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

def categorize_time(dt):
    hour = pd.to_datetime(dt).hour
    if 5 <= hour < 12:
        return 'morning'
    elif 12 <= hour < 17:
        return 'afternoon' 
    elif 17 <= hour < 21:
        return 'evening'
    else:
        return 'night'

df['time_of_day'] = df['dt'].apply(categorize_time)

st.dataframe(df)

