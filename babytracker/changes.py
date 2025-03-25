from flask import (Blueprint, g, render_template)

bp = Blueprint("changes", __name__, url_prefix = "/changes")

@bp.route("/")
def index():
    return render_template("changes/index.html")

