# shopping_basket

## Task to do

Task is to implement backend application library to product catalog and shopping basket of a web shop.

Product catalog contains at least names, amounts for sale (i.e. stock) and prices of available products.
Shopping basket contains products from catalog and to­be­purchased amounts.
Keep the product catalog up to date: products and stocks are updated based on the reservations in the basket.

Implement the following functions:

1. Adding/removing/editing products in product catalog

2. Adding/removing/editing products in shopping basket

3. Querying products from product catalog with basic pagination (e.g. 100 products / query), sorted by given sorting key (name or price).

4. Querying products from product catalog, grouped by price ranges (with a single functioncall,
   fully customizable via input data, example of range set: cheaper than 5 €, 5­10€,
   more expensive than 10€).

5. Searching product from catalog by matching the beginning of product name,
   filtering the results within given price range (min, max), and sorting by given key (name or price).

# The solution

## Used technologies

PYTHON, FLASK, SQLALCHEMY, MYSQL.
And of course we used python virtualenv.

## Create the environment in ubuntu

    sudo apt-get install mysql-server
    sudo apt-get install libmysqlclient-dev
    sudo apt-get install virtualenv
    sudo apt-get install python-pip python-dev build-essential
    sudo pip install --upgrade pip
    sudo pip install --upgrade virtualenv

## Create a root user in MySQL

First, use the mysql program to connect to the server as the MySQL root user:


    mysql --user=root mysql


If you have assigned a password to the root account, you must also supply a --password or -p option.

All what you have to do is to create a webshop database.

    mysql -u root -p
    create database webshop;

Next edit src/shop.py, there is

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://u_user:u_password@localhost/webshop'

u_user should be root (or what is you admin user)
and u_password is the password of the admin user.

REAMRK that here is a security risk, you have put here password in plain language.

## Run the service

Before you run the service you have create a virtual environment.
In shopping_basket directory give commands

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

And run the service

    cd src
    python run.py

The service is now running at localhost:5000

#API

| | |
| ------------- |:-------------:|
| URL  | / |
| What | Just for testing that service responses 200 OK|
| Example | curl -X GET http://localhost:5000/ |
| URL  | /add_product/ |
| What | Adds one product to database |
| Example | curl -X POST -H "Content-Type: application/json" -d '{"name":"Table", "amount":"9", "price":"25"}' http://localhost:5000/add_product/ |
| URL  | /remove_product/ |
| What | Removes one product from database |
| Example | curl -X POST -H "Content-Type: application/json" -d '{"name":"Table"}' http://localhost:5000/remove_product/ |
| URL  | /edit_product/ |
| What | Changes the price and amount of a product in database |
| Example | curl -X POST -H "Content-Type: application/json" -d '{"name":"Table", "amount":"120", "price":"20"}' http://localhost:5000/edit_product/ |
| URL  | /add_to_basket/ |
| What | Adds product to basket (you need a cookie, -c to create a new cookie, -b to use a cookie) |
| Example | curl -X POST -c cookie.txt -H "Content-Type: application/json" -d '{"name":"Chair", "amount":"4"}' http://localhost:5000/add_to_basket/|
| URL  | /remove_from_basket/ |
| What | Removes product from basket (-b to use your cookie)|
| Example | curl -X POST -b cookie.txt -H "Content-Type: application/json" -d '{"name":"Chair"}' http://localhost:5000/remove_from_basket/|
| URL  | /edit_basket/ |
| What | Change the amount of a product in your basket (-b to use your cookie)|
| Example | curl -X POST -b cookie.txt -H "Content-Type: application/json" -d '{"Name":"Table", "amount":"6"}' http://localhost:5000/edit_basket/ |
| URL  | /get_products_paginate/sort/sort_item/page/page_number/ |
| What | Queries products from database with basic pagination (now 5 products per page)|
| | sort_item can 'name' or 'price' |
| | page_number is the page number what you want |
| Example | curl -X GET http://localhost:5000/get_products_paginate/sort/name/page/1/
| URL  | /get_products_price_range/from-to/ |
| What | Queries products from database, grouped by price ranges |
| | Range could be 10-50. Or 25-. Or -99. Range is fully customizable |
| Example | curl -X GET http://localhost:5000/get_products_proce_range/200-300/ |
| URL  | /get_matchproducts_range_and_sort/product/name/range/from_to/sort/sort_item/ |
| What | Searches product from db by matching the beginning of product name, filtering the results within given price range (min-max), and sorting by given key (name or price). |
| Example | curl -X GET http://localhost:5000/get_matchproducts_range_and_sort/product/Ta/range/0-200/sort/name/|

MORE coming soon ...

#Testing

##Manual testing, use curl, for example

Create data into database
    curl -X POST -H "Content-Type: application/json" -d '{"name":"Table", "amount":"10", "price":"25"}' http://localhost:5000/add_product/

Do shopping (REMARK you need a file for cookie)!
First time use -c option, and next always -b option

    curl -X POST -c cookie.txt -H "Content-Type: application/json" -d '{"name":"Table", "amount":"1"}' http://localhost:5000/add_to_basket/

    curl -X POST -b cookie.txt -H "Content-Type: application/json" -d '{"name":"Table", "amount":"3"}' http://localhost:5000/edit_basket/

##Unit test




#Sorry for short instructions (at the moment)
