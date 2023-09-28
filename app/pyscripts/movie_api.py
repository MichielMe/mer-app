import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.environ.get("OMDDB_KEY")


def get_movie(movie_name):
    url = "http://www.omdbapi.com/"
    
    params = {
        "apikey": api_key,
        "t": movie_name,
    }
    
    response = requests.get(url, params=params)
    
    return response.json()



