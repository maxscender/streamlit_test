import streamlit as st
import pandas as pd

df = pd.read_csv('BASKET/basket_2024-11-13.csv')

# Method 1: Using column_config
st.dataframe(
    df,
    column_config={
        "Column1": st.column_config.TextColumn(
            "New Column Title",
            help="Hover text description",
            width="medium",
        ),
        "NumericColumn": st.column_config.NumberColumn(
            "Number",
            format="%.2f",
            width="small",
        ),
    },
    hide_index=True,
    use_container_width=True
)

#----------
