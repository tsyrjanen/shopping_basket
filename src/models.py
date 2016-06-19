#from app.shop import db
from shop import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)
    
    def __init__(self, id, name, amount, price):
        self.id = id
        self.name = name
        self.amount = amount
        self.price = price

    def as_dict(self):
        return {'name' : self.name, 'amount' : self.amount, 'price' : self.price}
