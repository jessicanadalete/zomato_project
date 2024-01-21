
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

#filtering the best restaurants

df_rest = df1.groupby(['restaurant_name','cuisines','restaurant_id','country_name','city','average_cost_for_two','votes'])['aggregate_rating'].max().reset_index()
df1_rest = df_rest.sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
df1_rest.reset_index(drop=True, inplace=True)

st.header('Cuisines Vision 🍽️')

st.markdown('#### Best Restaurants and Cuisines')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.markdown(f"<p font-size: 20px; '> {df1_rest.loc[0]['cuisines']} : {df1_rest.iloc[0]['restaurant_name']}</p>", unsafe_allow_html=True)

        note_1 = df1_rest.loc[0]['aggregate_rating']
        st.markdown(f"<p style='color:black; font-family: Arial, sans serif; font-size: 30px;'> {note_1}/5.0</p>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            f"<p font-size: 20px; '> {df1_rest.iloc[1]['cuisines']} : {df1_rest.iloc[1]['restaurant_name']}</p>",
            unsafe_allow_html=True)
        note_2 = df1_rest.iloc[1]['aggregate_rating']
        st.markdown(f"<p style='color:black; font-family: Arial, sans serif; font-size: 30px;'> {note_2}/5.0</p>",
                    unsafe_allow_html=True)

    with col3:
        st.markdown(
            f"<p font-size: 20px; '> {df1_rest.iloc[2]['cuisines']} : {df1_rest.iloc[2]['restaurant_name']}</p>",
            unsafe_allow_html=True)
        note_3 = df1_rest.iloc[2]['aggregate_rating']
        st.markdown(f"<p style='color:black; font-family: Arial, sans serif; font-size: 30px;"
                    f"'> {note_3}/5.0 </p>", unsafe_allow_html=True)

    with col4:
        st.markdown(
            f"<p font-size: 20px; '> {df1_rest.iloc[3]['cuisines']} : {df1_rest.iloc[3]['restaurant_name']}</p>",
            unsafe_allow_html=True)
        note_4 = df1_rest.iloc[3]['aggregate_rating']
        st.markdown(f"<p style='color:black; font-family: Arial, sans serif; font-size: 30px;'> {note_4}/5.0</p>",
                    unsafe_allow_html=True)

    with col5:
        st.markdown(
            f"<p font-size: 20px; '> {df1_rest.iloc[4]['cuisines']} : {df1_rest.iloc[4]['restaurant_name']}</p>",
            unsafe_allow_html=True)
        note_5 = df1_rest.iloc[4]['aggregate_rating']
        st.markdown(f"<p style='color:black; font-family: Arial, sans serif; font-size: 30px;'> {note_5}/5.0</p>",
                    unsafe_allow_html=True)

#sidebar filter1
country_options = st.sidebar.multiselect('Choose the countries you want to see the restaurants:', ['India', 'Australia', 'Brazil', 'Canada', 'Indonesia', 'New Zealand',
                                          'Philippines', 'Qatar', 'Singapore', 'South Africa', 'Sri Lanka',
                                          'Turkey', 'United Arab Emirates', 'England', 'United States of America'], default=['India','Brazil','England','South Africa','Indonesia'])
#country filter1
rows_select = df1['country_name'].isin(country_options)
df1 = df1.loc[rows_select,:]
st.sidebar.markdown("""___""")

#sidebar filter2
number_rest_slider = st.sidebar.slider('How many restaurants do you want to see?', min_value=1, max_value=20, value=10)
st.sidebar.markdown("""___""")

#sidebar filter3
cuisines_options = st.sidebar.multiselect('Cuisines:', ['African', 'American', 'Arabian', 'Argentine', 'Asian',
                                                             'Asian Fusion', 'Australian', 'Author', 'BBQ', 'Bakery',
                                                             'Bar Food', 'Balti', 'Beverages', 'Biryani', 'Bengali', 'Brazilian',
                                                             'Breakfast', 'British', 'Burger', 'Burman', 'Cafe', 'Cafe Food',
                                                             'Cajun', 'California', 'Canadian', 'Caribbean', 'Cantonese',
                                                             'Charcoal Chicken', 'Chinese', 'Chettinad', 'Coffee', 'Coffee and Tea',
                                                             'Contemporary', 'Continental', 'Creole', 'Cuban', 'Crepes', 'Deli', 'Dim Sum',
                                                             'Dimsum', 'Desserts', 'Diner', 'Döner', 'Donuts', 'Drinks Only', 'Durban',
                                                             'Eastern European', 'Egyptian', 'European', 'Fast Food', 'Finger Food',
                                                             'Fish and Chips', 'French', 'Fresh Fish', 'Fusion', 'Giblets', 'German',
                                                             'Gourmet Fast Food', 'Goan', 'Greek', 'Grill', 'Healthy Food', 'Home-made',
                                                             'Ice Cream', 'Indian', 'Indonesian', 'International', 'Italian', 'Izgara',
                                                             'Japanese', 'Juices', 'Kebab', 'Kiwi', 'Kokoreç', 'Korean', 'Korean BBQ',
                                                             'Latin American', 'Lebanese', 'Lucknowi', 'Maharashtrian', 'Malaysian',
                                                             'Malwani', 'Mandi', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Mineira',
                                                             'Modern Australian', 'Modern Indian', 'Mongolian', 'Moroccan', 'Momos',
                                                             'New American', 'New Mexican', 'North Eastern', 'North Indian', 'Others',
                                                             'Ottoman', 'Pakistani', 'Pan Asian', 'Parsi', 'Patisserie', 'Peruvian',
                                                             'Pizza', 'Polish', 'Portuguese', 'Pub Food', 'Rajasthani', 'Ramen',
                                                             'Restaurant Cafe', 'Roast Chicken', 'Russian', 'Salad', 'Sandwich',
                                                             'Scottish', 'Seafood', 'Singaporean', 'Sri Lankan', 'Southern', 'Spanish',
                                                             'Steak', 'Sunda', 'Sushi', 'Taco', 'Taiwanese', 'Tapas', 'Tea', 'Tex-Mex',
                                                             'Thai', 'Turkish', 'Turkish Pizza', 'Vegetarian', 'Vietnamese',
                                                             'Western', 'World Cuisine', 'Yum Cha'], default=['Italian','European', 'American', 'Korean'])

#cuisine filter
rows_select = df1['cuisines'].isin(cuisines_options)
df2 = df1.loc[rows_select,:]


with st.container():
    st.markdown("## Top"+ " "+ str(number_rest_slider) + " " + "Best Restaurants of the World")

    filtered_df = df2[df2['cuisines'].str.contains('|'.join(cuisines_options), case=False, na=False)]
    df_aux = filtered_df.groupby(['restaurant_name','cuisines','restaurant_id','country_name','city','average_cost_for_two','votes'])['aggregate_rating'].max().reset_index()
    df1_aux = df_aux.sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
    df1_aux_filtered = df1_aux.head(number_rest_slider) #combining the dataframe and the slider filter
    st.dataframe(df1_aux_filtered)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.header("Top"+ " "+ str(number_rest_slider) + " " + "Best Cuisines")
        df_aux = df1.groupby('cuisines')['aggregate_rating'].mean().reset_index()
        df_aux = df_aux.sort_values(by='aggregate_rating', ascending=False).head(number_rest_slider)

        fig1 = px.bar(df_aux, x='cuisines', y='aggregate_rating', text='aggregate_rating')
        fig1.update_traces(texttemplate='%{text:.2f}')
        fig1.update_layout(xaxis_title='Cuisines',
                           yaxis_title='Mean Aggregate Rating')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.header("Top"+ " "+ str(number_rest_slider) + " " + "Worst Cuisines")
        df_aux = df1.groupby('cuisines')['aggregate_rating'].mean().reset_index()
        df_aux = df_aux.sort_values(by='aggregate_rating', ascending=True).head(number_rest_slider)

        fig1 = px.bar(df_aux, x='cuisines', y='aggregate_rating', text='aggregate_rating')
        fig1.update_traces(texttemplate='%{text:.2f}')
        fig1.update_layout(xaxis_title='Cuisines',
                           yaxis_title='Mean Aggregate Rating')
        st.plotly_chart(fig1, use_container_width=True)
