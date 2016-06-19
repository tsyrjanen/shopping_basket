from flask_testing import TestCase
from flask import Flask,session
import mock
import json

from shop import app

from basket_functions import *

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

    def test_shop_responsing_with_cookie_ok(self):
        #Just to test that everything works, checks also cookie
        result = self.test_app.get('/')
        self.assertEqual(result.status_code, 200)
        if 'Set-Cookie' in result.headers:
            if 'session=' in result.headers['Set-Cookie']:
                print "OK session id  is",result.headers['Set-Cookie'].split('session=')[1].split(';')[0]
            else:
                self.assertTrue(False, "Could not find session id")
        else:
            self.assertTrue(False, "Could not find Cookie")

    @mock.patch('api.db_create_product')
    def test_add_product_OK(self, mock_db_create_product):
        mock_db_create_product.return_value = True
        mydata = {"name":"Car", "amount":"12", "price": "30300"}
        rv = self.test_app.post('/add_product/', data=json.dumps(mydata),
                                content_type='application/json')
        self.assertEqual(rv.status_code,200)

    @mock.patch('api.db_create_product')
    def test_add_product_not_OK(self, mock_db_create_product):
        mock_db_create_product.return_value = False
        mydata = {"name":"Car", "amount":"12", "price": "30300"}
        rv = self.test_app.post('/add_product/', data=json.dumps(mydata),
                                content_type='application/json')
        self.assertEqual(rv.status_code,403)

if __name__ == '__main__':
    unittest.main()
