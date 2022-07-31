import streamlit as st
from predict_page import show_predict_page
from data_visualization_page import plot_graphs
#plot_graphs()

#show_predict_page()


st.title('Site Energy Intensity Prediction')

page = st.selectbox('Select Page', options=['Prediction Page', 'Data Visualization Page' ]  )

if page=='Prediction Page':
    show_predict_page()
elif page=='Data Visualization Page':
    plot_graphs()
