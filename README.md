# shopping_basket
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

# Something about the solution

Implemented with PYTHON, FLASK, SQLALCHEMY

In src/shop.py there is

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://u_user:u_password@localhost/webshop'

that is for connetion to MySQL database (what you have to do manually is to create a user u_user with password u_password, and create also webshop database).

Remark also to create virtual environmet:
$virtualenv venv

$source venv/bin/activate

$pip install -r requirements.txt

And run the service (in your local machine in port 5000):

$python run.py

Manual testing, use curl, for example

Create data into database: curl -X POST -H "Content-Type: application/json" -d '{"name":"Table", "amount":"10", "price":"25"}' http://localhost:5000/add_product/

Do shopping (REMARK you need a file for cookie)!
First time use -c option, and next always -b option

curl -X POST -c cookie.txt -H "Content-Type: application/json" -d '{"name":"Table", "amount":"1"}' http://localhost:5000/add_to_basket/

curl -X POST -b cookie.txt -H "Content-Type: application/json" -d '{"name":"Table", "amount":"3"}' http://localhost:5000/edit_basket/


Sorry for short instructions (at the moment)
