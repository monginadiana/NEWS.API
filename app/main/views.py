from flask import render_template
from . import main
from ..request import get_sources,get_articles

@main.route('/')
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


@main.route('/articles/<source_id>')
def articles(source_id):
   

    '''
    View movie page function that returns the source details page and its data
    '''
    articles = get_articles(source_id)
    # print(articles)
    return render_template('article.html', articles= articles)