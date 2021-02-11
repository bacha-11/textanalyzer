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


