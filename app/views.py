from flask import render_template
from app import app

from .request import get_sources 


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_sources = get_sources()
    upcoming_source = get_sources()
    now_showing_sources = get_sources()
    title = 'Home - Welcome to The best News Article Website Online'
    return render_template('index.html', title = title, popular = popular_sources, upcoming = upcoming_source, now_showing = now_showing_sources )


@app.route('/news/<int:news_id>')
def source(source_id):

    '''
    View source page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)