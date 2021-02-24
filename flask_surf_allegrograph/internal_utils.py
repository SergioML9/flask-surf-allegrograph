from flask import current_app

def get_allegrograph_session():
    with current_app.app_context():
        try:
            return current_app.extensions["surf-allegrograph"]["session"]
        except KeyError:
            raise RuntimeError(
                "You must initiliaze an Allegrograph session"
            )