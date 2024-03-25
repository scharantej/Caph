
# Flask Application Generator
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('menu'))

@app.route('/menu')
def menu():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    coffee = request.form.get('coffee')
    tea = request.form.get('tea')
    cake = request.form.get('cake')
    return render_template('order.html', coffee=coffee, tea=tea, cake=cake)

@app.route('/confirm', methods=['POST'])
def confirm():
    return render_template('confirm.html')

if __name__ == "__main__":
    app.run(debug=True)
