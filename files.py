import streamlit as st
import pandas as pd

st.subheader("Loading the CSV file")
df = st.file_uploader("Upload the CSV file : ",type = ['csv','xlsx'])

df = pd.read_csv('C:/Users/nares/Desktop/streamlit/Tweets.csv')

if df is not None:
    st.table(df.head())

st.subheader("Dealing with images")
st.image("C:/Users/nares/Desktop/streamlit/presentation.png")

st.subheader("Dealing with images while uploading")
img_file = st.file_uploader("Upload the Image file : ",type=['png','jpeg'])

if img_file is not None:
    st.image(img_file)
