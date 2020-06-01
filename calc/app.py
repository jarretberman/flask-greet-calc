# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.add(a,b))

@app.route('/sub')
def sub_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.sub(a,b))
    
@app.route('/mult')
def mult_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.mult(a,b))
    
@app.route('/div')
def div_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.div(a,b))

@app.route('/math/<oper>')
def math_funcs(oper):
    a = int(request.args['a'])
    b = int(request.args['b'])
    ops = { 
        'add' : operations.add(a,b),
        'sub' : operations.sub(a,b),
        'mult' : operations.mult(a,b),
        'div' : operations.div(a,b),
    }

    return str(ops[oper])
    # if oper == 'add':
    #     return str(operations.add(a,b))
    # if oper == 'sub':
    #     return str(operations.sub(a,b))
    # if oper == 'mult':
    #     return str(operations.mult(a,b))
    # if oper == 'div':
    #     return str(operations.div(a,b))