import streamlit as st
import pandas as pd

primary_button = st.button(label="primary", type="primary")
secondary_button = st.button(label="secondary", type="secondary")

df = pd.read_csv("08_input_widgets/sample.csv")

if primary_button:
    st.line_chart(df, x="year", y=["col1", "col2", "col3"])

if secondary_button:
    st.write("Click on button 1 to show the graph")

st.divider()

checkbox = st.checkbox("Akshat")

if checkbox:
    st.write("Hi Akshat")
else:
    st.write("Hi new user")

st.divider()

radio = st.radio("Choose a column",
                 options=df.columns[1:], index=1, horizontal=True)
st.write(radio)

st.divider()

select = st.selectbox("Choose a column", options=df.columns[1:], index=0)
st.write(select)

st.divider()

multiselect = st.multiselect("Choose as many columns as you want",
                             options=df.columns[1:], default="col1", max_selections=2)
st.write(multiselect)

st.divider()

slider = st.slider("Pick a number", min_value=0, max_value=10, value=5, step=1)
st.write(f"The number you picked was ---> {slider}")

st.divider()

num_input = st.number_input("Type A Number", min_value=0, max_value=10)
st.write(num_input)

st.divider()

text_area = st.text_area("Write Your Message Here !!!",
                         height=200, placeholder="Write Your Message Here")
st.write(text_area)
