# wsgi.py
from flask import Flask, jsonify, abort, request

app = Flask(__name__)
the_products = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'Nothing' },
    { 'id': 4, 'name': 'Here.tv' }
]

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def get_products():

    return jsonify(the_products)

@app.route('/api/v1/products/<id_product>')
def get_product(id_product):
    for elem in the_products:
        if elem['id'] == int(id_product):
            return jsonify(elem)
    abort(404)

@app.route('/api/v1/products/<id_product>', methods=['DELETE'])
def delete_product(id_product):
    for elem in the_products:
        if elem['id'] == int(id_product):
            the_products.remove(elem)
            return ('', 204)
    abort(404)

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    the_products.append({'id' : request.form['id'], 'name' : request.form['name']})
    return('',201)
