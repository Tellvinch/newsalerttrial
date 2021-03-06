from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the news page and its data
    '''

    title = 'Home - Welcome to the most trusted news website online.'
    return render_template('news.html', title = title)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    title = f'You are viewing {news_id}'
    return render_template('news.html',title = title)