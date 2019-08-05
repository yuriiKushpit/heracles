from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/",methods = ['GET'])
def main():
    return render_template("index.html")


@app.route('/format',methods = ['POST', 'GET'])
def format():
    format = request.form['data']
    return render_template("format.html",formatted_value = format)


if __name__ == "__main__":
    app.run()
