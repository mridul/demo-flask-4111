from flask import Flask, render_template, request, redirect

from db_layer import get_names
import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    names_from_db = get_names()
    time = datetime.datetime.now()
    return render_template("home.html", names=names_from_db, var1=time)
