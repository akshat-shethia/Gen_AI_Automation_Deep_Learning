import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("07_charting_elements/sample.csv")

st.line_chart(df, x="year", y=["col1", "col2", "col3"])

st.divider()

st.area_chart(df, x="year", y=["col1", "col2"])

st.divider()

st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

st.divider()

geo_df = pd.read_csv("07_charting_elements/sample_map.csv")
st.map(geo_df)


st.divider()

fig, ax = plt.subplots()
ax.plot(df.year, df.col1)
ax.set_title("My figure title")
ax.set_xlabel("x label")
ax.set_ylabel("y label")
fig.autofmt_xdate()

st.pyplot(fig)
