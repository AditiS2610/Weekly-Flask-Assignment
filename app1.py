## Question 2

# **User Input Handling**:

#    Create a Flask application that takes a user's name as input through a form and displays a personalized greeting message. The form should be accessible at `/input` and should use the POST method to submit the data to another route.

from flask import Flask, render_template, request, redirect, url_for

app1 = Flask(__name__)

@app1.route('/input', methods=['GET', 'POST'])
def input_name():
    if request.method == 'POST':
        user_name = request.form['name']
        return redirect(url_for('greet', name=user_name))
    return render_template('input.html')

@app1.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app1.run(debug=True)
