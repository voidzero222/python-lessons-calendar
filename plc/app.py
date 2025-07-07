from flask import Flask, render_template, redirect
from werkzeug import Response

app = Flask(__name__)


@app.route("/")
def index() -> Response:
    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard() -> str:
    return "Dashboard"


@app.route("/dashboard/manage")
def manage_student() -> str:
    return "Manage student"
