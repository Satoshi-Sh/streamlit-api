from streamlit.connections import ExperimentalBaseConnection
import requests


class ApiConnection(ExperimentalBaseConnection):

    def _connect(self, **kwargs) -> requests.Session:
        session = requests.Session()
        session.headers['Authorization'] = 'Bearer ' + kwargs['token']
        return session

    def get_spotify_artist(self, artist_name):
        # API endpoint for searching artists
        search_url = "https://api.spotify.com/v1/search"

        # Set up the search parameters
        params = {
            "q": artist_name,
            "type": "artist"
        }

        # Make the API call using the 'requests' library
        response = self._instance.get(search_url, params=params)

        # Check if the API call was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON to extract the artist ID
            response_data = response.json()
            artists = response_data.get("artists", {}).get("items", [])
            if artists:
                # Return the first artist's ID (you may want to handle multiple results differently)
                return artists[0]
        else:
            # Handle error scenarios here
            return None

    # def get_artists(self, artist_id: str):
    #     # Construct the API URL
    #     api_url = f"https://api.spotify.com/v1/artists/{artist_id}"

    #     # Make the API call using the 'requests' library
    #     response = self._instance.get(api_url)

    #     # Check if the API call was successful (status code 200)
    #     if response.status_code == 200:
    #         return response.json()
    #     else:
    #         # Handle error scenarios here
    #         return None
