from flask import Flask

def create_app():
    # Init app
    app = Flask(__name__)

    # Register routes
    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/")

    return app