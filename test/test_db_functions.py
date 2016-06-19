from flask_testing import TestCase
from flask import Flask,session
import mock

from shop import app

from db_functions import *

class BasketTests(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.secret_key = 'some_secret'
        SQLALCHEMY_DATABASE_URI = 'sqlite://'
        return app

    def setUp(self):
        self.test_app = app.test_client()

    def tearDown(self):
        pass

    def test_validate_range_more_than_OK(self):
        self.assertTrue(validate_range('100-'))

    def test_validate_range_more_than_fails(self):
        self.assertFalse(validate_range('100'))
    
    def test_validate_range_between_OK(self):
        self.assertTrue(validate_range('100-200'))

    def test_validate_range_between_fails(self):
        self.assertFalse(validate_range('200-100'))

    def test_create_product_OK(self):
        name = 'Car'
        amount = 12
        price= 30300
        self.assertTrue(db_create_product(name, amount, price))
        
    def test_create_product_amount_is_ascii(self):
        name = 'Car'
        amount = 'xyz'
        price= 30300
        self.assertFalse(db_create_product(name, amount, price))

    def test_create_product_price_is_ascii(self):
        name = 'Car'
        amount = 12
        price= 'XYZ'
        self.assertFalse(db_create_product(name, amount, price))

if __name__ == '__main__':
    unittest.main()
