#app.py

from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

expenses = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/')
def add_expense();
    name = request.form['name']
    amount = float(request.form['amount'])
    category = request.form['category']

    expenses.append({'name': name, 'amount': amount, 'category' : category})

    return redirect(url_for('home'))

@app.route('/generate_pie_chart')
def generate_pie_chart():
    category_totals = {}
    for expenses in expenses:
        category = expense['category']
        amount = expense['amount']
        category_totals[category] = category_totals.get(category,0) + amount

        labels = category_totals.keys()
        sizes = category_totals.values()

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        img_buf = io.bytesIO()
        plt.savefig(img_buf, format='png')
        img_buf.seek(0)
        img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')
        pit.close()


if __name__ == '__main__':
    app.run(debug=True)