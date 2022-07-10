from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)


@app.route('/add')
def do_add():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route('/sub')
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)


@app.route('/mult')
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)


@app.route('/div')
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)


@app.route('/math/<operation>')
def all_in_one(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    if operation == 'add':
        result = add(a, b)
        return str(result)

    elif operation == 'sub':
        result = sub(a, b)
        return str(result)

    elif operation == 'mult':
        result = mult(a, b)
        return str(result)

    elif operation == 'div':
        result = div(a, b)
        return str(result)

    else:
        return "ERROR: Use operations (add, sub, mult, div) ONLY!"
