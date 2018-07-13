from kano_blog import app

# application factory
def create_app(test_config=None):
    return app.app
