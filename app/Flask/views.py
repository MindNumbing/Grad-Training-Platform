from flask import render_template
from app.Flask import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/new_order')
def new_order():
    return render_template('new_order.html')


@app.route('/orders')
def orders():
    return render_template('orders.html')


@app.route('/access')
def access():
    return render_template('access.html')
