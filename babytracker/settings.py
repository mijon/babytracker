from flask import (Blueprint, render_template, request, url_for, redirect)
from babytracker.db import get_db
from datetime import (datetime)
import pytz

bp = Blueprint("settings", __name__, url_prefix="/settings")


@bp.route("/", methods=("GET", "POST"))
def index():
    db = get_db()

    current_timezone = db.execute(
        "SELECT setting_value FROM settings WHERE setting_name='timezone'").fetchone()
    current_timezone = current_timezone["setting_value"]

    if request.method == "POST":
        newtz = request.form["txselect"]
        db.execute(
            "REPLACE INTO settings (setting_name, setting_value) VALUES ('timezone', ?)", newtz)
        redirect(url_for("settings.index"))

    return render_template("settings/index.html", timezones=pytz.all_timezones, current_timezone=current_timezone)
