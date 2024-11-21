from flask import Flask
from app.utils.env_loader import load_env

# Load environment variables early
load_env()

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object("config.Config")

    # Register routes
    with app.app_context():
        from .routes import ui_bp
        app.register_blueprint(ui_bp)

    return app
