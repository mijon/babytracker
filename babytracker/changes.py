from flask import (Blueprint, render_template, request, url_for, redirect)
from babytracker.db import get_db
from babytracker.settings import get_timezone
import babytracker.time_utils as tu

bp = Blueprint("changes", __name__, url_prefix="/changes")


@bp.route("/", methods=("GET", "POST"))
def index():
    db = get_db()

    if request.method == "POST":
        change_type = request.form["change-options"]

        # timestamp = datetime.now().isoformat()
        timestamp = tu.utc_timestamp()
        db.execute(
            "INSERT INTO changes (change_type, change_time)"
            " VALUES (?, ?)",
            (change_type, timestamp))
        db.commit()
        return redirect(url_for("changes.index"))

    changes = db.execute(
        "SELECT change_type, change_time FROM changes ORDER BY id DESC"
    ).fetchall()

    display_timezone = get_timezone()

    new_changes = []
    for row in changes:
        # row["change_time"] = tu.timestamp_to_tz(
        #     row["change_time"], display_timezone)
        new_changes.append({"change_time": tu.timestamp_to_tz(row["change_time"], display_timezone),
                            "change_type": row["change_type"]})

    return render_template("changes/index.html", changes=new_changes)
