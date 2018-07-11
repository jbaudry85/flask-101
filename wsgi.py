# wsgi.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    the_products = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' }
]
    return jsonify(the_product)        )
