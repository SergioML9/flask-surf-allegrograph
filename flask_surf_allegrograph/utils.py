from flask_surf_allegrograph.internal_utils import get_allegrograph_session
from flask import current_app

def get_session():
    with current_app.app_context():
        return get_allegrograph_session()