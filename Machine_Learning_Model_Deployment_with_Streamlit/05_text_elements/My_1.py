import streamlit as st

st.title("Akshat's Practice Page")

st.header("Main Header")

st.subheader("Sub Header")

st.markdown("### This ~has~ been `written` via **markdown**")

st.markdown("- Point 1")

st.code("""
        import pandas as pd
        df = pd.read_csv("Akshat.csv")
        df.head(10)""")

st.text("No formatting text")

st.divider()
st.latex("x^2 = 2x + 4y^e")
st.divider()

st.write("A little formatted default text")

