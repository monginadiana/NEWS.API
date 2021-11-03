import os


class Config:
    """
    General configuration parent class
    """

    NEWS_API_BASE_URL = "https://newsapi.org/v2/sources?apiKey={}"
    NEWS_API_ARTICLES_URL ="https://newsapi.org/v2/top-headlines?sources={}apiKey={}"
    NEWS_API_KEY = "57a2b9719c234580b841e4780b772d43"

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {"development": DevConfig, "production": ProdConfig}
