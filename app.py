from flask import Flask, render_template, request
from fractions import Fraction

app = Flask(__name__)


# Home route to render the calculator page
@app.route('/')
def home():
    return render_template('index.html')


# Conversion route
@app.route('/convert', methods=['POST'])
def convert():
    feet_text = request.form['feet']
    inches_text = request.form['inches']

    try:
        feet = int(feet_text) if feet_text else 0
        inches = float(Fraction(inches_text)) if inches_text else 0
        decimal_feet = feet + (inches / 12)
        result = decimal_feet * 1.207  # Assuming nefeet as a unit
        result_text = f"Result: {result:.3f} nefeet"
    except ValueError:
        result_text = "Invalid input"

    return render_template('index.html', result=result_text)


if __name__ == "__main__":
    app.run(debug=True)
