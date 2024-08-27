import streamlit as st
import pandas as pd

df = pd.read_csv("06_data_display_elements/sample.csv")

st.dataframe(df)
st.table(df)
st.write(df)

st.divider()

# Like a KPI chart in PowerBI
st.metric(label="KPI", value=10, delta=20, delta_color="normal")

st.divider()

st.metric(label="OPP Label", value=10, delta=-20, delta_color="inverse")
