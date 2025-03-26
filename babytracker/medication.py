from flask import (Blueprint, g, render_template)

bp = Blueprint("medication", __name__, url_prefix="/medication")


@bp.route("/")
def index():
    medications = ["paracetemol", "ibuprofen"]
    return render_template("medication/index.html", medications=medications)
