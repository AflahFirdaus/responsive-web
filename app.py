# Import Flask
from flask import Flask, render_template

# Main app
app = Flask(__name__)

# Set route default
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/daftar")
def daftar():
    return render_template("daftar.html")

@app.route("/produk1")
def produk1():
    return render_template("produk1.html")

# Debung, untuk automatic update server
if __name__ == "__main__":
    app.run(debug=True)