from flask import current_app

def get_allegrograph_session():
    try:
        return current_app.extensions["surf-allegrograph"]["session"]
    except KeyError:
        raise RuntimeError(
            "You must initiliaze an Allegrograph session"
        )