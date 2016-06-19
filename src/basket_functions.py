from flask import session
from db_functions import db_decrease_amount, db_increase_amount

def create_basket():
    if not 'basket' in session:
        session['basket'] = dict()

def basket_add_product(name, amount):
    create_basket()
    if not name in session['basket']:
        try:
            amount = int(amount)
            if db_decrease_amount(name, amount):
                session['basket'][name]=amount
                return True
        except ValueError:
            pass

    return False

def basket_remove_product(name):
    create_basket()
    if name in session['basket']:
        if db_increase_amount(name, session['basket'][name]):
            del session['basket'][name]
            return True
    return False

def basket_edit_product(name, amount):
    create_basket()
    if name in session['basket']:
        try:
            amount = int(amount)
            if amount < session['basket'][name]:
                if db_increase_amount(name, session['basket'][name] - amount):
                    session['basket'][name]=amount
                    return True
            elif amount > session['basket'][name]:
                if db_decrease_amount(name, amount - session['basket'][name]):
                    session['basket'][name]=amount
                    return True
            else:
                return True
        except ValueError:
            pass
    return False
