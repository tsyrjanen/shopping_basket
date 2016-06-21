from flask_testing import TestCase
from flask import Flask,session
import mock

from shop import app

from basket_functions import *

class BasketTests(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.secret_key = 'some_secret'
        #SQLALCHEMY_DATABASE_URI = 'sqlite://'
        return app

    def setUp(self):
        self.test_app = app.test_client()

    def tearDown(self):
        pass

    def test_no_basket_create_basket(self):
        self.assertFalse('basket' in session)
        create_basket()
        self.assertTrue('basket' in session)

    @mock.patch('basket_functions.db_decrease_amount')
    def test_add_product_OK(self, mock_db_decrease_amount):
        mock_db_decrease_amount.return_value = True
        self.assertTrue(basket_add_product('XYZ', 50))

    @mock.patch('basket_functions.db_decrease_amount')
    def test_add_product_not_in_db(self, mock_db_decrease_amount):
        #also tests when amount in db is too small
        mock_db_decrease_amount.return_value = False
        self.assertFalse(basket_add_product('x', 1))

    def test_add_product_already_in_basket(self):
        basket_add_product('xxxyyy', 1)
        self.assertFalse(basket_add_product('xxxyyy', 1))

    def test_add_product_amount_is_not_int(self):
        self.assertFalse(basket_add_product('foobar', 'xyz'))

if __name__ == '__main__':
    unittest.main()
