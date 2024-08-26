import streamlit as st
import pandas as pd

df = pd.read_csv("06_data_display_elements/sample.csv")

st.dataframe(df)
