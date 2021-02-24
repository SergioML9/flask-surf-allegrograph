from flask import current_app

def get_allegrograph_session():
    try:
        with current_app.app_context():
            return current_app.extensions["surf-allegrograph"]["session"]
    except KeyError:
        raise RuntimeError(
            "You must initiliaze an Allegrograph session"
        )