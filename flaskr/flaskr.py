#coding=utf-8
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import os
from db import User, Alticle,Dboj
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

# create our little application :)
app = Dboj.getapp()

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

app.secret_key = 'why would I tell you my secret key?'
#res= User.query.with_entities(User.password).all()
#print res

@app.route('/')
def show_entries():
    #db = get_db()
    #cur = db.execute('select title, text from entries order by id desc')
    #entries = cur.fetchall()
    entries=Alticle.query.with_entities(Alticle.title,Alticle.text).all()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    print request.form['title']
    new_alticlee=Alticle(userId=12,title=request.form['title'],text=request.form['text'])
    #db = get_db()
    #db.execute('insert into entries (title, text) values (?, ?)',
    #          [request.form['title'], request.form['text']])
    #db.commit()
    db=Dboj.getdb()

    db.session.add(new_alticlee)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        res=User.query.filter_by(username=request.form['username'],password=request.form['password']).first()
        print res
        if res==None:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run(debug=True)
