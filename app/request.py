# from app import app

# # Getting api key
# api_key = app.config['NEWS_API_KEY']
from app import app
import urllib.request,json

from app.source_test import Source
from .models import source

Source = source.Source
# Getting api key
api_key = app.config['MOVIE_API_KEY']

# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]