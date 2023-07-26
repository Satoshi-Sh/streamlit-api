import streamlit as st
import requests


@st.cache_data(ttl="30m")
def getToken():
    auth_url = "https://accounts.spotify.com/api/token"
    auth_data = {
        'grant_type': "client_credentials",
        'client_id': st.secrets['CLIENT_ID'],
        'client_secret': st.secrets['CLIENT_SECRET']
    }
    auth_response = requests.post(auth_url, data=auth_data)
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']
