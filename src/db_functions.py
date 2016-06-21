from shop import db
from models import Products
from sqlalchemy import *

def Max(a, b): return a if a > b else b

def validate_int(numbers):
    for i in numbers:
        try:
            int(i)
        except ValueError:
            return False
    return True

def validate_range(range):
    #input could be for example '5-' or '5-10' or '10-'
    #'5-' produces [5,0] and it means more expensive than 5
    #'5-10' produces [5,10] and it means price between 5 and 10
    #'10-' produces [0,10] and it means cheaper than 10
    #No valid range returns empty list

    if '-' in range and len(range.split('-'))==2:
        ok = True
        ranges = []
        for r in range.split('-'):
            try:
                ranges.append(int(r))
            except ValueError:
                if r == '':
                    ranges.append(0)
                else:
                    ok = False
        if ok:
            if (ranges[0] == 0 and ranges[1] > 0) or \
            (ranges[0] > 0 and ranges[1] == 0) or \
            (ranges[0] <= ranges[1]):
                return ranges
    return []

def db_create_product(name, amount, price):
    #Here we could also check existence of the product (do not allow duplicate name)
    if validate_int((amount,price)):
        new_product = Products(None, name, amount, price)
        db.session.add(new_product)
        db.session.commit()
        return True
    return False

def db_remove_product(name):
    product = Products.query.filter(Products.name == name).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        return True
    return False

def db_edit_product(name, amount, price):
    if validate_int((amount,price)):
        product = Products.query.filter(Products.name == name).first()
        if product:
            product.amount = amount
            product.price = price
            db.session.commit()
            return True
    return False

def db_decrease_amount(name, amount):
    if validate_int((amount,)):
        product = Products.query.filter(Products.name == name).first()
        if product:
            if product.amount >= amount:
                product.amount = product.amount - amount
                db.session.commit()
                return True
    return False

def db_increase_amount(name, amount):
    if validate_int((amount,)):
        product = Products.query.filter(Products.name == name).first()
        if product:
            product.amount = product.amount + amount
            db.session.commit()
            return True
    return False

def db_paginate_products(sort_item, page):
    if not sort_item in ['name', 'price']:
        sort_item = 'name'

    return Products.query.order_by(sort_item).paginate(
        Max(page, 1), 5, False).items

def db_products_price_range(range):
    ranges = validate_range(range)
    if ranges:

        query = db.session.query(Products)

        if ranges[1] == 0:
            #5- is ranges = [5,0] means more expensive than 5
            query = query.filter(Poduct.price > ranges[0])
        elif ranges[0] == 0:
            #-10 is ranges == [0,10] means cheaper than 10
            query = query.filter(Products.price > ranges[1])
        else:
            #5-10 is ranges == [5,10] means price between 5 and 10
            query = query.filter(and_(Products.price >= ranges[0],
                                 Products.price <= ranges[1]))
        #return jsonify(json_list=[i.as_dict() for i in query])
        return query

    return []

def db_match_products_range_and_sort(name, range, sort_item):
    if not sort_item in ['name', 'price']:
        sort_item = 'name'

    query = db_products_price_range(range)
    if query:
        if not name[-1] == '%':
            name = name + '%'
        query = query.filter(Products.name.like(name)).order_by(sort_item)

        return query

    return []
