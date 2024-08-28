import streamlit as st
import time
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Caching demonstration")

st.button('Test cache')

st.subheader("st.cache_data")

st.subheader("st.cache_resource")

st.cache_data


def cache_():
    time.sleep(2)
    return "I'm Done Running"


st.write(cache_())


@st.cache_resource
def LR():
    time.sleep(2)
    X = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
    Y = np.array([1, 2, 3, 4, 5, 6, 7])

    model = LinearRegression().fit(X, Y)
    return model


lr = LR()
X_pred = np.array([8]).reshape(-1, 1)
Y_pred = lr.predict(X_pred)

st.write(f"The Prediction is : {Y_pred[0]}")
