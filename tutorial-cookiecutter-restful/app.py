from flask import Flask
from tutorial-cookiecutter-restful import api
from tutorial-cookiecutter-restful import auth
from tutorial-cookiecutter-restful.extensions import apispec
from tutorial-cookiecutter-restful.extensions import db
from tutorial-cookiecutter-restful.extensions import jwt
from tutorial-cookiecutter-restful.extensions import migrate


def create_app(testing=False):
    """Application factory, used to create application"""
    app = Flask("tutorial-cookiecutter-restful")
    app.config.from_object("tutorial-cookiecutter-restful.config")

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app)
    configure_apispec(app)
    register_blueprints(app)

    return app


def configure_extensions(app):
    """configure flask extensions"""
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)


def configure_apispec(app):
    """Configure APISpec for swagger support"""
    apispec.init_app(app, security=[{"jwt": []}])
    apispec.spec.components.security_scheme(
        "jwt", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    )
    apispec.spec.components.schema(
        "PaginatedResult",
        {
            "properties": {
                "total": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": "string"},
                "prev": {"type": "string"},
            }
        },
    )


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)
