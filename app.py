from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        result = perform_operation(num1, num2, operation)
        return render_template('calculator.html', result=result, num1=num1, num2=num2, operation=operation)

    return 'Invalid Request'

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
            return 'Cannot divide by zero'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

