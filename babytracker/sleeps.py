from flask import (Blueprint, g, render_template)

bp = Blueprint("sleeps", __name__, url_prefix = "/sleeps")

@bp.route("/")
def index():
    return render_template("sleeps/index.html")
