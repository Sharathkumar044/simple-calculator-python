from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    scientific_func = request.form['scientific_func']

    result = perform_operation(num1, num2, operation)
    scientific_result = perform_scientific_function(result, scientific_func)

    entry = f"{num1} {operation} {num2} = {result}, Scientific Function: {scientific_func} Result: {scientific_result}"

    return render_template('calculator.html', result=result, num1=num1, num2=num2, operation=operation,
                           scientific_result=scientific_result, selected_func=scientific_func, entry=entry)

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    else:
        return None

def perform_scientific_function(value, func):
    import math
    if func == 'sqrt':
        return math.sqrt(value)
    elif func == 'sin':
        return math.sin(math.radians(value))
    elif func == 'cos':
        return math.cos(math.radians(value))
    elif func == 'tan':
        return math.tan(math.radians(value))
    else:
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
