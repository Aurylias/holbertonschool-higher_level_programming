"""Create a Basic HTML Template with Flask"""
from flask import Flask, render_template, request
import json
import csv

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
    with open('items.json') as file:
        itemList = json.load(file)
    return render_template('items.html', items=itemList.get('items', []))

def readJson(filename):
    with open(filename) as file:
        return json.load(file)

def readCsv(filename):
    products = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
        return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    if source == 'json':
        data = readJson('products.json')
    elif source == 'csv':
        data = readCsv('products.csv')
    else:
        return render_template('product_display.html', error='Wrong source')
    
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                   error='Product not found')
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html',
                                   error='Product not found')
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
