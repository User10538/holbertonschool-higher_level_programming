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
    matrix = []
    if request.args.get('source') == 'json':
        with open('products.json', 'r') as f:
            data = json.load(f)
        if request.args.get('id'):
            matrix = [row for row in data if row['id'] == int(request.args.get('id'))]
        else:
            matrix = data
    elif request.args.get('source') == 'csv':
        with open('products.csv', mode='r', newline='') as f:
            data = csv.DictReader(f)
            matrix = [row for row in data]
        if request.args.get('id'):
            matrix = [row for row in matrix if row['id'] == request.args.get('id')]
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
        matrix = [{key: value for key, value in zip(fields, row)} for row in res]
        conn.close()
    else:
        matrix = 'error'
    if len(matrix) == 0:
        matrix = 'no product'
    return render_template('product_display.html', data=matrix)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
