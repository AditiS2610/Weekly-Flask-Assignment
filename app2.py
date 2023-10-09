from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('items.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

def get_items():
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    return items

def add_item(name):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

@app.route('/items')
def list_items():
    items = get_items()
    return render_template('items.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item_route():
    if request.method == 'POST':
        name = request.form['name']
        if name:
            add_item(name)
    return redirect(url_for('list_items'))

if __name__ == '__main__':
    app.run(debug=True)
