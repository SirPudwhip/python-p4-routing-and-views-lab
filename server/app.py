#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<parameter>')
def count_route(parameter):
    x = int(parameter)
    i = 0
    new_list = []

    for i in range(x):
        new_list.append(f"{i}\n")
        i += 1

    final = "".join(new_list)
    print(final)

    return(f'{final}')

@app.route('/math/<parameters>')
def math(parameters):
    list1 = []
    list1[:0] = parameters
    a = int(list1[0])
    b = int(list1[-1])
    c = list1[1]
    
    if c == "+":
        return_var = a + b
        return(f'{return_var}')

    if c == "-":
        return_var = a - b
        return(f'{return_var}')    

    if c == "*":
        return_var = a * b
        return(f'{return_var}')

    if c == "d":
        return_var = a / b
        return(f'{return_var}')

    if c == "%":
        return_var = a % b
        return(f'{return_var}')



if __name__ == '__main__':
    app.run(port=5555, debug=True)

