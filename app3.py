from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = [
    {'username': 'user1', 'password': 'password1', 'name': 'User One'},
    {'username': 'user2', 'password': 'password2', 'name': 'User Two'},
]
def is_valid_credentials(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if is_valid_credentials(username, password):
            return redirect(url_for('dashboard', username=username))
        else:
            error_message = "Invalid username or password. Please try again."
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    user_name = next((user['name'] for user in users if user['username'] == username), None)
    if user_name:
        return f'Welcome, {user_name}! This is your dashboard.'
    else:
        return 'User not found.'

if __name__ == '__main__':
    app.run(debug=True)