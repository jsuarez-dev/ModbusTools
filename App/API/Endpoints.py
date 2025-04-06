from flask import jsonify
from flask import Blueprint

bp = Blueprint("API",__name__)


@bp.route("/api/")
def index():
    return jsonify({ "data": "data"})
