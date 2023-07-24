import streamlit as st
from custom_connection import ApiConnection
from dataframe import extract_data
from auth import getToken
import pandas as pd


# Title of the app
st.title('Stremlit meets Spotify')
access_token = getToken()
conn = st.experimental_connection(
    "spotify-api", type=ApiConnection, token=access_token)
# print(extract_data(conn.get_spotify_artist_id('radio head')))

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
        [st.session_state.df, new_df], ignore_index=True)
    name_input = ""

if not st.session_state.df.empty:
    st.dataframe(st.session_state.df)
