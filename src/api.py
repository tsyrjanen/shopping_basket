from flask import request, Response, session, jsonify
from shop import app, db
from basket_functions import basket_add_product, basket_remove_product, basket_edit_product
from db_functions import db_create_product, db_remove_product, db_edit_product, db_paginate_products, db_products_price_range, db_match_products_range_and_sort
import json

@app.route('/', methods=['GET'])
def root():
    print "Hello world."
    return Response(status=200)

@app.route('/add_product/', methods=['POST'])
def add_product():
    content = request.get_json()
    try:
        if db_create_product(content['name'], content['amount'], content['price']):
            return Response(status=200)
    except KeyError:
        pass
    return Response(status=403)

@app.route('/remove_product/', methods=['POST'])
def remove_product():
    content = request.get_json()
    try:
        if db_remove_product(content['name']):
            return Response(status=200)
    except KeyError:
        pass
    return Response(status=403)

@app.route('/edit_product/', methods=['POST'])
def edit_product():
    content = request.get_json()
    try:
        if db_edit_product(content['name'], content['amount'], content['price']):
            return Response(status=200)
    except KeyError:
        pass
    return Response(status=403)

@app.route('/add_to_basket/', methods=['POST'])
def add_to_basket():
    content = request.get_json()
    try:
        if basket_add_product(content['name'], content['amount']):
            return jsonify(session['basket'])
    except KeyError:
        pass
    return Response(status=403)

@app.route('/remove_from_basket/', methods=['POST'])
def remove_from_basket():
    content = request.get_json()
    try:
        if basket_remove_product(content['name']):
            return jsonify(session['basket'])
    except KeyError:
        pass
    return Response(status=403)

@app.route('/edit_basket/', methods=['POST'])
def edit_basket():
    content = request.get_json()
    try:
        if basket_edit_product(content['name'], content['amount']):
            return jsonify(session['basket'])
    except KeyError:
        pass
    return Response(status=403)

@app.route('/get_products_paginate/', methods=['GET'])
@app.route('/get_products_paginate/sort/<sort_item>/', methods=['GET'])
@app.route('/get_products_paginate/sort/<sort_item>/page/<int:page>/', methods=['GET'])
def paginate_products(sort_item='name', page=1):
    return jsonify(json_list=[i.as_dict() for i in
                              db_paginate_products(sort_item, page)])

@app.route('/get_products_price_range/<range>/', methods=['GET'])
def products_price_range(range):
    return jsonify(json_list=[i.as_dict() for i in
                              db_products_price_range(range)])

@app.route('/get_matchproducts_range_and_sort/product/<name>/range/<range>/sort/<sort_item>/', methods=['GET'])
def matchproducts_range_and_sort(name='', range='', sort_item='name'):
    return jsonify(json_list=[i.as_dict() for i in
                              db_match_products_range_and_sort(name, range, sort_item)])
