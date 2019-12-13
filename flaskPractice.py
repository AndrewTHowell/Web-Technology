# Section: Flask app

from flask import Flask, redirect, url_for, request, render_template, flash, session
import os
import pandas as pd

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
    df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})
    return render_template('books.html', tables=[df.to_html(classes='data', header="true")])

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
    app.run()

# Section End
