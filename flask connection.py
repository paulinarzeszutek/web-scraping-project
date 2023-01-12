from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def table():
    return render_template("table_with_shopping_data_v1.html")