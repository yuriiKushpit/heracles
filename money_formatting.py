from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")


@app.route('/format', methods=['POST', 'GET'])
def format():
    format = "{:,.2f}".format(float(request.form['data'])).replace(",", " ")
    return render_template("format.html", formatted_value=format.replace(',','.'))


if __name__ == "__main__":
    app.run()
