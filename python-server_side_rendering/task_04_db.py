from flask import Flask, render_template, request
import sqlite3
import json, csv

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
    with open('items.json', 'r') as file:
        data = json.load(file)

        item_list = data.get("items", [])
    return render_template('items.html', items=item_list)
    # "items" can be used in items.html

# read json
def read_json():
    with open('products.json', 'r') as file:
        data = json.load(file)
    return data
# read csv
def read_csv():
    with open('products.csv', newline='', encoding='utf-8') as file:
        product_list = []
        csv_file = csv.DictReader(file)
        for row in csv_file:
            product_list.append(row)
    return product_list
# read sql
def read_sql(p_id=None):
    try:
        database = sqlite3.connect('products.db')
        cursor = database.cursor()

        if p_id:
            cursor.execute("SELECT * FROM products WHERE id=?", (p_id,))
        else:
            cursor.execute("SELECT * FROM products")

        products = cursor.fetchall()
        product_list = [{'id': product[0], 'name': product[1], 'category': product[2], 'price': product[3]} for product in products]
        return product_list
    except sqlite3.Error as error:
        print(f"Error: {error}")
        return None
    finally:
        database.close()

# route /products
@app.route('/products', methods=['GET'])
def products():
    source = request.args.get('source').lower()
    p_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql(p_id)

    if p_id:
        try:
            # p_id = int(p_id) # convert type to use in loop
            filtered_products = [product for product in products if str(product['id']) == p_id]

            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid product id")
    else:
        filtered_products = products

    return render_template('product_display.html', products=filtered_products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
