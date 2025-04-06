from flask import (Blueprint, render_template, request, url_for, redirect)
from babytracker.db import get_db
from datetime import timedelta
import babytracker.time_utils as tu
from babytracker.settings import get_timezone

bp = Blueprint("feeds", __name__, url_prefix="/feeds")


@bp.route("/", methods=["GET", "POST"])
def index():
    db = get_db()

    if request.method == "POST":
        # feed_end = datetime.now()
        feed_end = tu.utc_timestamp()
        feed_duration = timedelta(hours=int(request.form["hour"]),
                                  minutes=int(request.form["minute"]),
                                  seconds=int(request.form["second"]),
                                  microseconds=int(request.form["count"]))
        feed_start = feed_end - feed_duration
        breast = request.form["breast"]
        db.execute("INSERT INTO feeds (start_time, stop_time, breast, duration)"
                   " VALUES (?, ?, ?, ?)",
                   (feed_start, feed_end, breast, str(feed_duration)))
        db.commit()

        return redirect(url_for("feeds.index"))

    feedlog = db.execute(
        "SELECT start_time, stop_time, duration, breast FROM feeds ORDER BY id DESC"
    ).fetchall()

    display_timezone = get_timezone()
    new_feedlog = []
    for row in feedlog:
        new_feedlog.append(
            {"start_time": tu.timestamp_to_tz(row["start_time"], display_timezone),
             "stop_time": tu.timestamp_to_tz(row["stop_time"], display_timezone),
             "duration": row["duration"],
             "breast": row["breast"]}
        )

    return render_template("feeds/index.html", feedlog=new_feedlog)
