import streamlit as st
import pandas as pd

cancer_data = pd.read_csv('cancer.csv')

st.write("Here's our first attempt at using data to create a table:")
st.write(cancer_data)
