import inflection
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('/Users/jessicanadalete/Documents/DSF/FTC_myproject/zomato.csv')

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


st.header('Countries Vision 🌎')

#Streamlit

#sidebar filter1
country_options = st.sidebar.multiselect(
    'Choose the countries you want to see the restaurants:', [
        'Australia', 'Brazil', 'Canada', 'England','India','Indonesia',
        'New Zealand', 'Philippines', 'Qatar', 'Singapore', 'South Africa',
        'Sri Lanka', 'Turkey', 'United Arab Emirates',
        'United States of America'],
    default=['Brazil','England','South Africa','Indonesia'])

#country filter
rows_select = df1['country_name'].isin(country_options)
df1 = df1.loc[rows_select,:]

#Page construction
with st.container():

    df_aux = df1.groupby('country_name')['restaurant_id'].nunique().reset_index()

    fig1 = px.bar(df_aux, x='country_name',
                  y='restaurant_id',
                  text='restaurant_id',
                  labels={'country_name': 'Country'},
                  title='Number of registered restaurants by country')

    fig1.update_layout(xaxis_title='Country',
                       yaxis_title='Number of restaurant',
                       xaxis={'categoryorder':'total descending'},
                       title={
                           'text': "Number of registered restaurants by country",
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font': {'size': 18}}
                       )
    st.plotly_chart(fig1, use_container_width=True)

with st.container():
    
    df_aux = df1.groupby('country_name')['city'].nunique().reset_index()

    fig1 = px.bar(df_aux, x='country_name',
                  y='city',
                  text='city',
                  labels={'country_name': 'Country'},
                  title='Number of registered cities by country')

    fig1.update_layout(xaxis_title='Country',
                       yaxis_title='Number of cities',
                       xaxis={'categoryorder':'total descending'},
                       title={
                           'text': "Number of registered cities by country",
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font': {'size': 18}})

    st.plotly_chart(fig1, use_container_width=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        df_aux = df1.groupby('country_name')['votes'].mean().reset_index()

        fig1 = px.bar(df_aux, x='country_name',
                      y='votes',
                      text='votes',
                      color='country_name',
                      labels={'country_name': 'Country'})
        fig1.update_traces(texttemplate='%{text:.2f}')
        fig1.update_layout(xaxis_title='Country',
                           yaxis_title='Votes average',
                           xaxis={'categoryorder': 'total descending'},
                           title='Votes average by country')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        df_aux = df1.groupby('country_name')['average_cost_for_two'].mean().reset_index()

        fig1 = px.bar(df_aux, x='country_name',
                      y='average_cost_for_two',
                      color='country_name',
                      labels={'country_name': 'Country'},
                      text='average_cost_for_two')

        fig1.update_traces(texttemplate='%{text:.2f}')
        fig1.update_layout(xaxis_title='Country',
                           yaxis_title='Cost for two average',
                           xaxis={'categoryorder': 'total descending'},
                           title='Cost for two average by country')
        st.plotly_chart(fig1, use_container_width=True)
