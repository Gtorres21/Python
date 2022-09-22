from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)  
app.secret_key = "No secrets on github"

@app.route('/')         
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    session['first_name']= request.form['first_name']
    session['last_name']= request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['strawberry'] = int(request.form['strawberry'])
    session['raspberry'] = int(request.form['raspberry'])
    session['apple'] = int(request.form['apple'])
    session['total'] = session['strawberry'] + session['raspberry'] + session['apple']
    print (f"Charging {session['first_name']} for {session['total']} fruits")
    return redirect('/show_info')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")


@app.route('/show_info')
def show_info():
    return render_template('checkout.html')




if __name__=="__main__":   
    app.run(debug=True)