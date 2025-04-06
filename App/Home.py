
from flask import Blueprint
from flask import render_template

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/", methods=("GET", "POST"))
def home():
    return render_template("home/index.html")
