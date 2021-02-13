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
        if request.form.get('find_length'):
            res = request.form['string']
            return render_template('string.html', title='Length', res=res)

        elif request.form.get('capitalize'):
            res = request.form['string']
            return render_template('string.html', cap_str=res)
            #return redirect(url_for('cap_string', res=res))

        elif request.form.get('upper'):
            res = request.form['string']
            text_upper = res.upper()
            return render_template('string.html', text_upper=text_upper)

        elif request.form.get('lower'):
            res = request.form['string']
            text_lower = res.lower()
            return render_template('string.html', text_upper=text_lower)

        elif request.form.get('encode_text'):
            res = request.form['string']
            text_encode = res.encode()
            return render_template('string.html', text_encode=text_encode)

        elif request.form.get('print'):
            res = request.form['string']
            print_able = res.isprintable()
            return render_template('string.html',  print_able=print_able, print=res)
    return render_template('string.html')


@app.route('/cap_string/<res>', methods=['POST', 'GET'])
def cap_string(res):
    if res:
        return render_template('string.html', cap_str=res)
    return render_template('string.html')


@app.route('/word_replace', methods=['GET', 'POST'])
def word_replace():
    if request.method == 'POST':
        all_string = request.form['string']
        old_word = request.form['old_word']
        new_word = request.form['new_word']
        return render_template('replace.html', title='Replace Word', all_string=all_string, old_word=old_word, new_word=new_word)
        
    return render_template('replace.html', title='Replace Word')





