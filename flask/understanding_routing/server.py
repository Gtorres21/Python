from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Hello World')
    return 'Hello World'

@app.route('/dojo')
def dojo():
    print('dojo')
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/<int:num>/<name>')
def repeat(num, name):
    name =(f' {name}')
    print(num,name)
    return num*name

@app.errorhandler(404)
def page_not_found(e):
    return "No website"





















if __name__=="__main__":
    app.run(debug=True)