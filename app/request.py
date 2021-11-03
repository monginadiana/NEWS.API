
import urllib.request,json

from .models import Articles

# from app.source_test import Source
from .models import Source 

api_key = ""
# Getting api key

base_url_source = None
# Getting the movie base url
base_url_articles = None

def configure_request(app):
    global api_key, base_url_source, base_url_articles
    base_url_source = app.config['NEWS_API_BASE_URL']
    base_url_articles = app.config['NEWS_API_ARTICLES_URL']
    api_key = app.config['NEWS_API_KEY']
    
# def configure_request(app):
#     global api_key,base_url
#     api_key = app.config['NEWS_API_KEY']
#     base_url = app.config['NEWS_API_BASE_URL']
def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey=57a2b9719c234580b841e4780b772d43'

    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

    
def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        language = source_item.get('language')
        
        sources_object = Source(id,name,description,url,category,country,language)

        source_results.append(sources_object)

    return source_results

def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = "https://newsapi.org/v2/top-headlines?sources={}&apiKey=57a2b9719c234580b841e4780b772d43".format(source_id)


    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    print(articles_results)

    return articles_results

def process_articles(articles_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    articles_results = []
    for source_item in articles_list:
        title = source_item.get('title')
        name = source_item.get('name')
        description = source_item.get('description')
        urlToImage= source_item.get('urlToImage')
        publishedAt= source_item.get('publishedAt')
        url =source_item.get('url')
     
      
        
        articles_object = Articles(title,name,description,urlToImage,url,publishedAt)

        articles_results.append(articles_object)

    return articles_results



