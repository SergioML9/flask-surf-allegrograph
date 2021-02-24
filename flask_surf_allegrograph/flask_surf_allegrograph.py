import surf
from flask import current_app, _app_ctx_stack


class SurfAllegrograph(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('AGRAPH_HOST', 'localhost')
        app.config.setdefault('AGRAPH_PORT', '10035')
        
        app.teardown_appcontext(self.teardown)

        session = self.connect()

        # Save this so we can use it later in the extension
        if not hasattr(app, "extensions"):  # pragma: no cover
            app.extensions = {}
        app.extensions["flask-surf-allegrograph"] = session

    def connect(self):
        store = surf.Store(reader = 'allegro_franz', 
                   writer = 'allegro_franz',
                   server = current_app.config['AGRAPH_HOST'],
                   port = current_app.config['AGRAPH_PORT'],
                   catalog = 'ewetasker',
                   repository = 'ewetasker-db')

        print('Create the session')
        session = surf.Session(store,{})
        return session

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'allegrograph_db'): #
            ctx.allegrograph_db.close()

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'allegrograph_db'):
                ctx.allegrograph_db = self.connect()
            return ctx.allegrograph_db