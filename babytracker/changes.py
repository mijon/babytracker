from flask import (Blueprint, render_template, request, url_for, redirect)
from babytracker.db import get_db
from datetime import datetime

bp = Blueprint("changes", __name__, url_prefix="/changes")


@bp.route("/", methods=("GET", "POST"))
def index():
    db = get_db()

    if request.method == "POST":
        change_type = request.form["change-options"]

        timestamp = datetime.now().isoformat()
        db.execute(
            "INSERT INTO changes (change_type, change_time)"
            " VALUES (?, ?)",
            (change_type, timestamp))
        db.commit()
        return redirect(url_for("changes.index"))

    changes = db.execute(
        "SELECT change_type, change_time FROM changes ORDER BY id DESC"
    ).fetchall()

    return render_template("changes/index.html", changes=changes)
