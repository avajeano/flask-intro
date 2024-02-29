from flask import flask
from operations import add, sub, mult, div
app = Flask(__name__)

"""Basic math operations"""

@app.route('/add')
def add_operation():
    """Add a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def sub_operation():
    """Subtract b from a"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route('/sub')
def mult_operation():
    """Multiply a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route('/sub')
def div_operation():
    """Divide a by b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)