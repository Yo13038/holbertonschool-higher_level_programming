#!/usr/bin/env python3
"""
Flask application extending Jinja templating to read from a JSON file.
"""
import json
import os
from flask import Flask, render_template

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
    """Reads items from items.json and passes them to the template."""
    items_list = []
    try:

        with open('items.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading items.json: {e}")

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
