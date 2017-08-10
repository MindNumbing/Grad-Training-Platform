from flask import render_template
from app.Flask import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', connection_status="connected")


@app.route('/orders')
def orders():
    return render_template('orders.html', connection_status="connected")


@app.route('/access')
def access():
    return render_template('access.html', connection_status="connected")
