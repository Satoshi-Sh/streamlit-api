import streamlit as st
from custom_connection import ApiConnection
from dataframe import extract_data
from auth import getToken
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# Title of the app
st.title('Stremlit meets Spotify')
access_token = getToken()
conn = st.experimental_connection(
    "spotify-api", type=ApiConnection, token=access_token)


# create dataframe to show retrieved data
columns = [
    "name",
    "popularity",
    "followers",
    "genres",
    "external_url",
]
data = pd.DataFrame(columns=columns)
data['popularity'] = data['popularity'].astype(float)
data['followers'] = data['followers'].astype(int)
if 'df' not in st.session_state:
    st.session_state.df = data

name_input = st.text_input("Enter an artist name:")
col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    button_clicked = st.button("Submit")

if button_clicked and name_input != '':
    data = conn.get_spotify_artist(name_input)
    new_row = extract_data(data)
    new_df = pd.DataFrame([new_row])
    st.session_state.df = pd.concat(
        [st.session_state.df, new_df], ignore_index=True).sort_values(by=["popularity", 'followers'], ascending=True)
    name_input = ""

if not st.session_state.df.empty:
    st.dataframe(st.session_state.df)
    st.session_state.df['followers'] = pd.to_numeric(
        st.session_state.df['followers'])
    # data viz
    # https://stackoverflow.com/questions/37930693/how-can-i-make-a-barplot-and-a-lineplot-in-the-same-seaborn-plot-with-different
    plt.style.use('default')
    ax1 = sns.set_style(style=None, rc=None)
    # Create the subplots
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot the line plot on ax1
    sns.pointplot(
        data=st.session_state.df, x='name', y='followers', ax=ax1, labe='followers')

    # Create the secondary y-axis on ax2
    ax2 = ax1.twinx()

    # Plot the bar plot on ax2
    sns.barplot(data=st.session_state.df, x='name',
                y='popularity', alpha=0.5, ax=ax2, label='popularity')

    # Show the plot
    st.pyplot(fig)
