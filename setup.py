from setuptools import find_packages
from setuptools import setup

__version__ = "0.1"

setup(
    name="tutorial-cookiecutter-restful",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "flask-restful",
        "flask-migrate",
        "flask-jwt-extended",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "python-dotenv",
        "passlib",
        "apispec[yaml]",
        "apispec-webframeworks",
    ],
    entry_points={"flask.commands": ["tutorial-cookiecutter-restful = tutorial-cookiecutter-restful.manage:cli"]},
)
