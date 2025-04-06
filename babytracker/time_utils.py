from datetime import (datetime, timezone)
import pytz


def utc_timestamp():
    # return (datetime.now(tz=timezone.utc).isoformat())
    return datetime.now(tz=timezone.utc)


def timestamp_to_tz(timestamp, tz):
    # dt = datetime.fromisoformat(timestamp)
    dt = timestamp

    # if there is no timezone, assume UTC
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=pytz.utc)

    converted = dt.astimezone(
        pytz.timezone(tz))
    return converted
