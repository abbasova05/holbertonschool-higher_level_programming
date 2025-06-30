#!/usr/bin/env python3
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def show_items():
    items_path = os.path.join(os.path.dirname(__file__), 'items.json')

    try:
        with open(items_path, 'r') as f:
            data = json.load(f)
            items = data.get("items", [])
    except Exception as e:
        print(f"Error reading JSON: {e}")
        items = []

    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
