import datetime
from flask import Flask, flash, redirect, render_template, request, url_for
from google.appengine.api import users
from models import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'LJL:Sdj374918 y8(*(*& BSNNNNSAIS*jp'
app.debug = True

def user_dict(key_name=None):
    user_dict = {
        'login_url': users.create_login_url(request.path),
        'logout_url': users.create_logout_url(url_for('index')),
        'user': users.get_current_user(),
    }
    if user_dict['user']:
        user_dict['user_id'] = user_dict['user'].user_id()
    if key_name:
        return user_dict[key_name]
    return user_dict


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/products/', methods=['GET', 'POST'])
def products():
    products = Products.query().filter().fetch()
    return render_template(
        'products.html',
        products=products,
        **user_dict())


@app.route('/add_product/', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name', None)
        name = name.lower()
        price = request.form.get('price', None)
        product = Products(name=name, price=price)
        product.put()
    return redirect(url_for('products'))


@app.route('/remove_product/<int:product_id>/', methods=['GET', 'POST'])
def remove_product(product_id):
    product = ndb.Key('Products', product_id)
    product.delete()
    return redirect(url_for('products'))

@app.route('/orders/<int:product_id>/', methods=['GET', 'POST'])
def orders(product_id):
    product = Products.get_by_id(int(product_id))
    if request.method == 'POST':
        order = int(request.form.get('order', 0))
        current_quntity = int(product.quntity)
        if request.form['submit'] == 'purchase':
            current_quntity += order
        elif request.form['submit'] == 'sale':
            current_quntity -= order
        else:
            pass # unknown
        product.quntity = str(current_quntity)
        product.total = str(current_quntity * int(product.price))
        product.put()
    return redirect(url_for('products'))