from flask import (Blueprint, render_template, request, url_for, redirect)
from babytracker.db import get_db
from datetime import (datetime)
import pytz

bp = Blueprint("settings", __name__, url_prefix="/settings")


@bp.route("/", methods=("GET", "POST"))
def index():
    db = get_db()
    if request.method == "POST":
        newtz = request.form["tzselect"]
        print(newtz)
        db.execute(
            "REPLACE INTO settings (setting_name, setting_value, setting_type) VALUES ('timezone', ?, 'string')",
            (newtz,))
        db.commit()
        redirect(url_for("settings.index"))

    current_timezone = db.execute(
        "SELECT setting_value FROM settings WHERE setting_name='timezone'").fetchone()
    current_timezone = current_timezone["setting_value"]

    return render_template("settings/index.html",
                           timezones=pytz.all_timezones,
                           current_timezone=current_timezone)


def get_timezone():
    db = get_db()
    tz = db.execute(
        "SELECT setting_value FROM settings WHERE setting_name = 'timezone'").fetchone()
    return tz["setting_value"]
