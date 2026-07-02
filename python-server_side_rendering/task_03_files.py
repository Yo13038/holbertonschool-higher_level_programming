#!/usr/bin/env python3
"""
Flask application that reads data from JSON and CSV files based on URL parameters.
"""
import os
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Reads and parses products.json"""
    if not os.path.exists('products.json'):
        return []
    with open('products.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def read_csv():
    """Reads and parses products.csv"""
    products = []

    base_dir = os.path.abspath(os.path.dirname(__file__))
    csv_path = os.path.join(base_dir, 'products.csv.txt')
    
    if not os.path.exists('csv_path'):
        return products
    with open('products.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:

            products.append({
                "id": int(row['id']),
                "name": row['name'],
                "category": row['category'],
                "price": float(row['price'])
            })
    return products


@app.route('/products')
def display_products():
    """Renders the product display page with filtering options."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    

    if source == 'json':
        products = read_json()
    else:
        products = read_csv()
        

    if product_id is not None:
        try:
            target_id = int(product_id)

            filtered_products = [p for p in products if p['id'] == target_id]
            
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            
            products = filtered_products
        except ValueError:

            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
