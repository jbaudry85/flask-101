# wsgi.py
from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def get_products():
    the_products = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Nothing' },
    { 'id': 4, 'name': 'Here.tv' }
]
    return jsonify(the_products)

@app.route('/api/v1/products/<id_product>')
def get_product(id_product):
    the_products = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Nothing' },
    { 'id': 4, 'name': 'Here.tv' }
]
    for elem in the_products:
        if elem['id'] == int(id_product):
            return jsonify(elem)
    abort(404)

@app.route('/api/v1/products/<id_product>', methods=['DELETE'])
def delete_product(id_product):
    the_products = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Nothing' },
    { 'id': 4, 'name': 'Here.tv' }
]
    for elem in the_products:
        if elem['id'] == int(id_product):
            the_products.remove(elem)
            return ('', 204)
    abort(404)
