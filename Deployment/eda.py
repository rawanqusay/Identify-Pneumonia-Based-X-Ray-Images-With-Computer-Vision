# import library
import streamlit as st
import pandas as pd
import numpy as np 
from PIL import Image

def run():
    # Set Title
    st.title('Pneumonia X-Rays Visualization')

    # memasukkan gambar
    st.image ('https://static.vecteezy.com/system/resources/previews/005/259/113/non_2x/diagnosing-pneumonia-word-concepts-banner-blood-tests-infographics-with-linear-icons-on-turquoise-background-isolated-creative-typography-outline-color-illustration-with-text-vector.jpg')

    # menampilkan EDA
    st.markdown('## Exploratory Data Analysis (EDA)')
    st.markdown ('---')
 
 
    # EDA 1
    st.markdown("<h3 style='text-align: center;'>Pneunomia X-Rays</h3>", unsafe_allow_html=True)

    image = Image.open('BACTERIA-1514320-0003.jpeg')
    st.image(image)
    
    st.write('---')

    # EDA 2
    st.markdown("<h3 style='text-align: center;'>Normal X-Rays</h3>", unsafe_allow_html=True)

    image = Image.open('NORMAL-831813-0001.jpeg')
    st.image(image)
    
    st.write('---')

    # EDA 3
    st.markdown("<h3 style='text-align: center;'>Distribusi Data Train</h3>", unsafe_allow_html=True)

    image = Image.open('EDA_Train.png')
    st.image(image)

    st.write('---')

if __name__ == "__main__":
    run()
    