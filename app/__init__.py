from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.utils.env_loader import load_env

# Load environment variables early
load_env()

# Initialize the database and migration tool
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object("config.Config")

    # Import models here to ensure they are registered with SQLAlchemy
    from app.models import User, Message  # Import models explicitly

    # Initialize the database and migration tool
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    with app.app_context():
        from .routes import ui_bp
        app.register_blueprint(ui_bp)

    # Register commands after the app is created to avoid circular import
    from app.commands.seed_settings_command import seed_settings_command
    app.cli.add_command(seed_settings_command)

    return app
