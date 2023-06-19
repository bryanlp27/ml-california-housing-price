import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="California Housing Price Prediction",
    page_icon="🚀"
)

st.title('California Housing Price Prediction')

if 'model' not in st.session_state:
    model = pickle.load(open('California-Housing-Prices-Regression-BryanLP.sav', 'rb'))
    st.session_state['model'] = model

median_income_input = st.number_input('Insert Median Income :100: :')
ocean_proximity_select = st.selectbox('Ocean Proximity :ocean: :', ['INLAND', 'NEAR BAY', '<1H OCEAN', 'NEAR OCEAN', 'ISLAND'])
person_in_house_input = st.number_input('Insert how many person in the House :house: :')
bedroom_in_house_input = st.number_input('Insert How many bedroom in the House :bed: :')
room_in_house_input = st.number_input('Insert How many room in the House :house_buildings: :')
housing_age_group_select = st.selectbox('Housing Age Group :cityscape: :', ['New Property', 'Small Renovation Property', 'Medium Renovation Property', 'Big Renovation Property', 'Antique / Old Property'])

if st.button('Model Predict'):
    data = pd.DataFrame({
        'median_income': [median_income_input],
        'ocean_proximity': [ocean_proximity_select],
        'person_in_house': [person_in_house_input],
        'bedroom_in_house': [bedroom_in_house_input],
        'room_in_house': [room_in_house_input],
        'housing_age_group': [housing_age_group_select]
    })
    
    result = st.session_state['model'].predict(data)
    st.write(f'Prediction model : ${result[0]}')
else:
    st.write('Please input the features above to start modeling')
