# from app import app

# # Getting api key
# api_key = app.config['NEWS_API_KEY']
from app import app
import urllib.request,json
from .models import source

Movie = source.Source