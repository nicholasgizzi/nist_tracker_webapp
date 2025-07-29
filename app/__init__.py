from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import Category

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nist_tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from . import routes
    app.register_blueprint(routes.bp)

    @app.context_processor
    def inject_nist_functions():
        # Make all NIST function categories available to templates
        funcs = Category.query.order_by(Category.id).all()
        return dict(nist_functions=funcs)

    return app