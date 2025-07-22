import sqlite3
import os, csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Helper function to read JSON data
def read_json_data():
    if not os.path.exists('products.json'):
        return []
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

#Helper function to read CSV data
def read_CSV_data():
     if not os.path.exists('products.csv'):
        return []
     
     with open('products.csv', encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)
            return list(csv_reader)

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
def show_items():
    items = []
    if os.path.exists('items.json'):
        with open('items.json', 'r') as file:
            data = json.load(file)
            items = data.get('items', [])
    return render_template('items.html', items=items)

@app.route('/products')
def get_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json_data()
    elif source == 'csv':
        data = read_CSV_data()
    else:
        error = "Wrong source. Please use 'json' or 'csv'."
        return render_template('product_display.html', error=error)
    
    # Optional ID filtering
    if product_id:
        data = [item for item in data if str(item.get('id')) == product_id]
        if not data:
            error = "Product not found"
            return render_template('product_display.html', products=[], error=error)

    return render_template('product_display.html', products=data)

def create_database():
    if os.path.exists('products.db'):
        os.remove('products.db')
        
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Products (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   category TEXT NOT NULL,
                   price REAL NOT NULL
                   )
                   ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
                   VALUES
                   (1, 'Laptop', 'Electronics', 799.99),
                   (2, 'Coffee Mug', 'Home Goods', 15.99)
                   ''')
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)    
        
