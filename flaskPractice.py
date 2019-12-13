# Section: Flask app

from flask import Flask, redirect, url_for, request, render_template, flash, session
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def passwordCorrect(userID, password):
    if userID == 17:
        if password == "hello":
            return True
    return False

@app.route('/user/')
def userPage():
    userID = session["userID"]
    return render_template('user.html', userID=userID)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        form = request.form
        userID = form["userID"]
        if userID.isdigit():
            userID = int(userID)
            password = form["password"]
            if passwordCorrect(userID, password):
                flash("Password accepted")
                session["userID"] = userID
                return redirect(url_for('userPage'))
            else:
                print("Password rejected")
                flash("Password rejected")
                return redirect(url_for('login'))
        else:
            print("Invalid userID")
            flash("Invalid userID")
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run()

# Section End
