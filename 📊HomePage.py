#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 18:42:47 2024

@author: jessicanadalete
"""


import folium
import inflection
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster


df = pd.read_csv('zomato.csv')

df1 = df.copy() #creating copy of original dataframe

#Cleaning the data
## Changing columns name
title = lambda x: inflection.titleize(x)
snakecase = lambda x: inflection.underscore(x)
spaces = lambda x: x.replace(" ", "")
cols_old = list(df1.columns)
cols_old = list(map(title, cols_old))
cols_old = list(map(spaces, cols_old))
cols_new = list(map(snakecase, cols_old))
df1.columns = cols_new

#Removing NaN from cuisines column
Cuisines_sem_nan = pd.notna (df1['cuisines'])
df1 = df1.loc[Cuisines_sem_nan,:].copy()

#Removing other options of cuisines and filtering only first option
df1["cuisines"] = df1.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

#Adding country names based on code
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zealand",
162: "Philippines",
166: "Qatar",
184: "Singapore",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

df1['country_name'] = df1['country_code'].apply(lambda x: COUNTRIES.get(x, None))

#streamlit

st.set_page_config(
    layout="wide",
    page_title="Zomato Project"
)

st.title('No Hunger! 🥗🍔')
st.header('The best place to find your newest favorite restaurant!')
st.markdown('#### Metrics on the platform:')

#Homepage
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown("Number of restaurants on platform")
        number_of_restaurants = df1.loc[:,'restaurant_id'].nunique()
        st.markdown(f"<p style='color:black; font-family: Arial, sans serif; font-size: 30px;'> {number_of_restaurants}</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("Number of countries on platform")
        number_of_countries = df1.loc[:,'country_code'].nunique()
        st.markdown(f"<p style='color:black; font-family: Arial, sans serif; font-size: 30px;'> {number_of_countries}</p>", unsafe_allow_html=True)

    with col3:
        st.markdown("Number of cities on platform")
        number_of_cities = df1.loc[:, 'city'].nunique()
        st.markdown(f"<p style='color:black; font-family: Arial, sans serif; font-size: 30px;'> {number_of_cities}</p>", unsafe_allow_html=True)

    with col4:
        st.markdown("Number of reviews on platform")
        number_of_votes = df1.loc[:, 'votes'].sum()
        formatted_number = "{:,.0f}".format(number_of_votes)
        st.markdown(f"<p style='color:black; font-family: Arial, sans serif; font-size: 30px;'> {formatted_number}</p>", unsafe_allow_html=True)

    with col5:
        st.markdown("Different types of cuisines")
        number_of_cuisines = df1.loc[:, 'cuisines'].nunique()
        st.markdown(f"<p style='color:black; font-family: Arial, sans serif; font-size: 30px;'> {number_of_cuisines}</p>", unsafe_allow_html=True)

with st.container():
    df_aux = df1[['country_name', 'restaurant_id', 'latitude', 'longitude']].drop_duplicates() # remove duplicates considering all columns

    map = folium.Map()
    marker_cluster = MarkerCluster().add_to(map) # grouping pins based on zoom

    for index, location_info in df_aux.iterrows():
        folium.Marker([location_info['latitude'], location_info['longitude']],
                      popup=location_info[['country_name', 'restaurant_id']]).add_to(marker_cluster)

    folium_static(map, width=1024, height=600)



st.sidebar.markdown("""___""")

st.sidebar.markdown(f"<p style='font-weight: bold; font-size: 25px'>{'🥗🍔 No Hunger'} </p>", unsafe_allow_html=True)


#sidebar filter
country_options = st.sidebar.multiselect('Choose the countries you want to see the restaurants:', ['Australia', 'Brazil',
                                                                                                   'Canada', 'England','India','Indonesia',
                                                                                                   'New Zealand', 'Philippines', 'Qatar', 'Singapore',
                                                                                                   'South Africa', 'Sri Lanka', 'Turkey',
                                                                                                   'United Arab Emirates',
                                                                                                   'United States of America'],
                                         default=['Brazil','England','South Africa','Indonesia'])
#country filter
rows_select = df1['country_name'].isin(country_options)
df1 = df1.loc[rows_select,:]

#Data download button

csv_data = df1.to_csv(index=False).encode('utf-8')

st.sidebar.download_button(
    label="Download Data",
    data=csv_data,
    mime='text/csv',
)
