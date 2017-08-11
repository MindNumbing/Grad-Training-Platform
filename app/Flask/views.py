from flask import render_template
from app.Flask import app
from app.FIX.client import fix_connection_test

connection = fix_connection_test.isConnected()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', connection_status=connection)


@app.route('/fix_connection_test', methods=['POST'])
def test_connection():
    fix_connection_test.connect_client('FIXT-1.1')
    return render_template('index.html', connection_status=connection)


@app.route('/new_order')
def new_order():
    return render_template('new_order.html', connection_status=connection)


@app.route('/orders')
def orders():
    return render_template('orders.html', connection_status=connection)


@app.route('/access')
def access():
    return render_template('access.html', connection_status=connection)
