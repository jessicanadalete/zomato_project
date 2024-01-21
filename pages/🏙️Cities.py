import inflection
import pandas as pd
import streamlit as st
import plotly.express as px

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


st.header('Cities Vision 🏙️')

#sidebar filter1

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

with st.container():

    df_aux = df1.groupby(['city','country_name'])['restaurant_id'].nunique().reset_index()
    df_aux1= df_aux.sort_values(by='restaurant_id', ascending=False)

    df_aux_top10 = df_aux1.head(10)

    fig1 = px.bar(df_aux_top10, x='city',
                  y='restaurant_id',
                  text='restaurant_id',
                  title='Cities with more restaurants',
                  labels={'country_name': 'Country'},
                  color='country_name')

    fig1.update_layout(xaxis_title='City',
                       yaxis_title='Number of restaurant',
                       xaxis={'categoryorder':'total descending'},
                       title={
                           'text': "Cities with the highest number of registered restaurants",
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font': {'size': 18}}
                       )

    st.plotly_chart(fig1, use_container_width=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:

        new_rows_select = df1.loc[:,'price_range'] >= 4
        df_aux = df1.loc[new_rows_select,['city','restaurant_id','country_name']].groupby(
            ['city', 'country_name'])['restaurant_id'].nunique().reset_index()

        df_aux1 = df_aux.sort_values(by='restaurant_id', ascending=False)

        df_aux_top = df_aux1.head()

        fig1 = px.bar(df_aux_top, x='city',
                      y='restaurant_id',
                      text='restaurant_id',
                      labels={'country_name': 'Country'},
                      title='Cities with note 4 restaurants',
                      color='country_name')

        fig1.update_layout(xaxis_title='City',
                           yaxis_title='Number of restaurant',
                           xaxis={'categoryorder': 'total descending'},
                           title={
                               'text': "Cities with the highest number of restaurants rated 4 or higher",
                               'y': 0.9,
                               'x': 0.5,
                               'xanchor': 'center',
                               'yanchor': 'top',
                               'font': {'size': 18}}
                           )

        st.plotly_chart(fig1, use_container_width=True)

    with col2:

        new_rows_select1 = df1.loc[:, 'price_range'] <= 2.5
        df_aux_ = df1.loc[new_rows_select1, ['city', 'restaurant_id', 'country_name']].groupby(
            ['city', 'country_name'])['restaurant_id'].nunique().reset_index()

        df_aux1 = df_aux_.sort_values(by='restaurant_id', ascending=False)

        df_aux_top_ = df_aux1.head()

        fig1 = px.bar(df_aux_top_, x='city',
                      y='restaurant_id',
                      text='restaurant_id',
                      labels={'country_name': 'Country'},
                      title='Cities with note 2.5 restaurants',
                      color='country_name')

        fig1.update_layout(xaxis_title='City',
                           yaxis_title='Number of restaurant',
                           xaxis={'categoryorder': 'total descending'},
                           title={
                               'text': "Cities with the highest number of restaurants with a rating of 2.5 or lower",
                               'y': 0.9,
                               'x': 0.5,
                               'xanchor': 'center',
                               'yanchor': 'top',
                               'font': {'size': 18}}
                           )

        st.plotly_chart(fig1, use_container_width=True)

with st.container():
    df_aux = df1.groupby(['country_name','city'])['cuisines'].nunique().reset_index()
    df_aux1 = df_aux.sort_values(by='cuisines', ascending=False)

    df_aux_cuisines = df_aux1.head(10)

    fig1 = px.bar(df_aux_cuisines, x='city',
                  y='cuisines',
                  text='cuisines',
                  labels={'country_name': 'Country'},
                  color='country_name')

    fig1.update_layout(xaxis_title='Country',
                       yaxis_title='Number of cities',
                       xaxis={'categoryorder':'total descending'},
                       title={
                           'text': "Cities with the greatest variety of cuisines",
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font': {'size': 18}
                           })
    st.plotly_chart(fig1, use_container_width=True)
