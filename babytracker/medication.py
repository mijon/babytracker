from flask import (Blueprint, render_template, request, redirect, url_for)
from babytracker.db import get_db
from datetime import datetime

bp = Blueprint("medication", __name__, url_prefix="/medication")


@bp.route("/", methods=("GET", "POST"))
def index():
    db = get_db()

    if request.method == "POST":
        # There are two forms on this page, so we need to check which we have
        if "medication-take-name" in request.form.keys():  # we're logging a take
            medication_taken = request.form["medication-take-name"]
            timestamp = datetime.now().isoformat()
            db.execute("INSERT INTO medications_log (medication, taken_date)"
                       " VALUES (?, ?)",
                       (medication_taken, timestamp))
            db.commit()
            redirect(url_for("medication.index"))

        else:
            med_name = request.form["medication-name"]
            duration_time = request.form["duration-number"]
            duration_text = request.form["duration-text"]

            db.execute("INSERT INTO medications (name, time_between_doses, unit_between_doses)"
                       " VALUES (?, ?, ?)",
                       (med_name, duration_time, duration_text))
            db.commit()
            redirect(url_for("medication.index"))

    medications = db.execute("SELECT name FROM medications;").fetchall()
    medications = [m["name"] for m in medications]

    medication_log = db.execute(
        "SELECT medication, taken_date FROM medications_log ORDER BY id DESC;").fetchall()

    return render_template("medication/index.html",
                           medications=medications,
                           medication_log=medication_log)
