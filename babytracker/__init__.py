import os
from flask import Flask
from flask import render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "babytracker.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello_world():
        return render_template("hello.html")

    from . import feeds
    app.register_blueprint(feeds.bp)

    from . import changes
    app.register_blueprint(changes.bp)

    from . import medication
    app.register_blueprint(medication.bp)

    from . import sleeps
    app.register_blueprint(sleeps.bp)

    from . import settings
    app.register_blueprint(settings.bp)

    from . import db
    db.init_app(app)

    return app
