from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "No secrets on github"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process():
    print(request.form)
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment_box']=request.form['comment_box']
    return redirect('/info')

@app.route('/info')
def info():
    return render_template('info.html')







if __name__=="__main__":
    app.run(debug=True)