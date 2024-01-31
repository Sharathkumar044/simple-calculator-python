from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        scientific_func = request.form['scientific_func']

        result = perform_operation(num1, num2, operation)
        scientific_result = perform_scientific_function(result, scientific_func)

        entry = f"{num1} {operation} {num2} = {result}, Scientific Function: {scientific_func} Result: {scientific_result}"

        return render_template('calculator.html', result=result, num1=num1, num2=num2, operation=operation,
                                scientific_result=scientific_result, selected_func=scientific_func, entry=entry)

    except ValueError as e:
        # Handle invalid input (non-numeric values)
        error_message = "Invalid input. Please enter numeric values."
        return render_template('calculator.html', error_message=error_message)

@app.route('/history')
def history():
    # Dummy history data, replace with actual history data
    history_entries = ["1 + 2 = 3", "3 * 4 = 12"]
    return render_template('history.html', history_entries=history_entries)

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

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
        return "Error: Invalid scientific function"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
