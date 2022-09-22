from flask import Flask, render_template, redirect,session

app = Flask(__name__)
app.secret_key = "No secrets on github"


@app.route('/')
def home():
    if 'num' not in session:
        session['num'] = 1
    else:
        session['num'] +=1
    return render_template('index.html')


@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)