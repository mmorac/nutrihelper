from flask import Flask, render_template, request, session
from flask_session import session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"



#DEFINE INDEX PAGE
@app.route("/")
def index():
    return render_template("index.html")

#DEFINE LOGIN PAGE
@app.route("/login", methods=["GET"])

def login():
    return render_template("login.html")

@app.route("/result", methods=["POST"])

def result():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")
    return render_template("result.html", usuario = usuario, clave = clave)
