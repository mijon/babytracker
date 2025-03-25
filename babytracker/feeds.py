from flask import (Blueprint, g, render_template)

bp = Blueprint("feeds", __name__, url_prefix = "/feeds")

@bp.route("/")
def index():
    return render_template("feeds/index.html")
