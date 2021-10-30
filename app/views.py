from flask import render_template
from app import app

from .request import get_sources 


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting news source
    technology_sources = get_sources('technology')
    business_sources = get_sources('business')
    sport_sources = get_sources('sports')

    title = 'Enjoy Your Daily Brief'

    return render_template('index.html', title = title, Tech = technology_sources, business = business_sources, sports= sport_sources )


@app.route('/news/<int:news_id>')
def source(source_id):

    '''
    View source page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)