import locale
from decimal import Decimal, ROUND_HALF_UP

locale.setlocale(locale.LC_ALL, '')
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")


@app.route('/format', methods=['POST', 'GET'])
def format():
    format = '{:n}'.format(
        Decimal(request.form['data']).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
    return render_template("format.html", formatted_value=format.replace(',','.'))


if __name__ == "__main__":
    app.run()
