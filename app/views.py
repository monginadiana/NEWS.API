from flask import render_template
from app import app

from .request import get_sources 


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting news source
    technology_sources = get_sources()
    business_sources = get_sources()
    sports_sources = get_sources()

    title = 'Enjoy Your Daily Brief'

    return render_template('index.html', title = title, technology = technology_sources, business = business_sources, sport = sports_sources )


@app.route('/news/<int:news_id>')
def source(source_id):

    '''
    View source page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)