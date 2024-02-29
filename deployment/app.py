# Import Library
import streamlit as st

# Import streamlit page
import eda
import prediction

# navigation
navigasi = st.sidebar.selectbox('Select Page :', 
                                ('Home Page','EDA','Diabetes Prediction'))
st.write('---')

if navigasi == 'Home Page':
    st.header('Home Page') 
    st.write('---')
    st.image('https://s3-publishing-cmn-svc-prd.s3.ap-southeast-1.amazonaws.com/article/hDenYkKK_tPJHcbLClhmh/original/027328700_1590718778-Ilustrasi-Diabetes-shutterstock_715778998.jpg')
    st.write('---')

    st.markdown('### Milestone 2')
    st.write('Creator   : Muhammad Hafidz Adityaswara')
    st.write('From      : HCK - 012')
    st.write('This project aims to develop a predictive model that can identify whether a patient has diabetes or not.')
    st.write('---')


elif navigasi == 'Diabetes Prediction':
    prediction.run()
else :
    eda.run()