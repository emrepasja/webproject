from flask import Blueprint, render_template

bp = Blueprint("home", __name__)

@bp.route("/", methods=[ "GET"])
def index():
    return render_template("home/index.html")

@bp.route("/about", methods=["GET"])
def about():
    return render_template("home/about.html")

@bp.route("/contact", methods=["GET"])
def contact():
    return render_template("home/contact.html")

