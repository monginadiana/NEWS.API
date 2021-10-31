from flask import render_template
from app import app

from .request import get_sources 
from .request import get_sources,get_source



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


@app.route('/source/<int:id>')
def source(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_source(id)
    title = f'{source.title}'

    return render_template('source.html',title = title,source = source)