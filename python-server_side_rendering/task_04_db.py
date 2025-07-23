from flask import Flask, render_template, request
import json
import csv

import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        items = json.load(f)
        return render_template('items.html', items=items)

@app.route('/products')
def products():
    data = []
    get_id = []
    if request.args.get('source') == 'json':
        with open('products.json', 'r') as f:
            data = json.load(f)
        if request.args.get('id'):
            get_id = [row for row in data if row['id'] == int(request.args.get('id'))]
        else:
            get_id = data
            
    elif request.args.get('source') == 'csv':
        with open('products.csv', mode='r', newline='') as f:
            data = csv.DictReader(f)
            get_id = [row for row in data]
        if request.args.get('id'):
            get_id = [row for row in get_id if row['id'] == request.args.get('id')]

    elif request.args.get('source') == 'sql':
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if request.args.get('id'):
            cursor.execute('SELECT * FROM Products WHERE id = ?', (request.args.get("id"), ))
        else:
            cursor.execute('''
                SELECT * FROM Products;
            ''')
        res = cursor.fetchall()
        fields = [column[0] for column in cursor.description]
        get_id = [{key: value for key, value in zip(fields, row)} for row in res]
        conn.close()
    else:
        get_id = 'error'
    if len(get_id) == 0:
        get_id = 'no product'
    return render_template('product_display.html', data=get_id)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
