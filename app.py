from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "About Us"

@app.route('/contact')
def contact():
    return "Contact Us"

if __name__ == '__main__':
    app.run(debug=True)
