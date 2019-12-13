# Section: Import modules

import pandas as pd

from os.path import dirname, abspath

import numpy as np

from scipy.sparse.linalg import svds

from flask import Flask, redirect, url_for, request, render_template, flash, session
import os

# Section End

# Section: Constants

CURRENTPATH = dirname(abspath(__file__))

# Section End

app = Flask(__name__)
app.secret_key = os.urandom(16)

def passwordCorrect(userID, password):
    if userID == 17:
        if password == "hello":
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books/')
def books():
    books = pd.read_csv(CURRENTPATH+"//books.csv")
    books = books.rename(columns={"bookID": 'ID',
                                  "bookTitle": 'Title',
                                  "bookGenre": 'Genres'})
    return render_template('books.html',
                           tables=[books.to_html(classes='table table-striped '
                           'table-hover table-responsive',
                           header=True, index=False)])

@app.route('/user/')
def userPage():
    if "logged_in" in session:
        if session["logged_in"]:
            userID = session["userID"]
            return render_template('user.html')
    else:
        session["logged_in"] = False
        flash("Please log in first")
        return redirect(url_for('index'))

@app.route('/logout/', methods=["POST"])
def logout():
    session["logged_in"] = False
    session["userID"] = None

    flash("Logged out")
    return redirect(url_for('index'))

@app.route('/login/', methods=["POST"])
def login():
    form = request.form
    userID = form["userID"]
    if userID.isdigit():
        userID = int(userID)
        password = form["password"]
        if passwordCorrect(userID, password):
            session["logged_in"] = True
            session["userID"] = userID
            return redirect(url_for('userPage'))
        else:
            flash("Password rejected")
            return redirect(url_for('index'))
    else:
        flash("Invalid userID")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=80)

# Section End
