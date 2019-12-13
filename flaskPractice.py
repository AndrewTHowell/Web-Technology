# Section: Flask app

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/user/')
def userPage(userID):
    return render_template('user.html', userID = userID)

@app.route('/loginResponse/')
def response(success):
    if success:

    return render_template('response.html',
                            title = title,
                            message)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        form = request.form
        userID = form["userID"]
        password = form["password"]
        if passwordCorrect(userID, password):
            flash("Password accepted")
            return redirect(url_for('user', userID = userID))
        else:
            flash("Password rejected")

    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run()

# Section End
