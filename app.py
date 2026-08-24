import streamlit as st
import pandas as pd

st.title("PC Builder")

components = pd.read_csv("components.csv")

st.write("Available Components")

st.dataframe(components)