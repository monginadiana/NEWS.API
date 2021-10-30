from flask import render_template
from app import app

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The bestnew article Website Online'
    return render_template('index.html', title = title)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = news_id)