from flask import Flask

app = Flask(__name__)

users = [
    {"id": 1, "ad": "Tahmina", "yas": 20}
    {"id": 2, "ad": "Zehra", "yas": 18}
]

@app.route('/')