from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import TextForm
from app.models import UserText




@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', title="Home")



@app.route('/find_length', methods=['GET', 'POST'])
def find_length():
    if request.method == 'POST':
        res = request.form['string']
        return render_template('string.html', title='Length', res=res)
    return render_template('string.html')


@app.route('/word_replace', methods=['GET', 'POST'])
def word_replace():
    if request.method == 'POST':
        all_string = request.form['string']
        old_word = request.form['old_word']
        new_word = request.form['new_word']
        return render_template('replace.html', title='Replace Word', all_string=all_string, old_word=old_word, new_word=new_word)

    return render_template('replace.html', title='Replace Word')





