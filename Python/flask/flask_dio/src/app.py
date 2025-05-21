import click
import os
import sqlalchemy as sa

from datetime import datetime
from flask import Flask, current_app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()

class User(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(sa.String(120), unique=True, nullable=False)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r}, active={self.active!r})"

class Post(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    created: Mapped[str] = mapped_column(sa.DateTime(timezone=True), server_default=sa.func.now())
    title: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    body: Mapped[str] = mapped_column(sa.String(500), nullable=False)
    author_id: Mapped[int] = mapped_column(sa.ForeignKey(("user.id")))

    def __repr__(self) -> str:
        return f"id={self.id!r}, title={self.title!r}, author_id={self.author_id!r})"


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    global db
    with current_app.app_context():
        db.create_all()
    click.echo('Initialized the database.')

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///dio_bank.sqlite',
        )
    

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #register CLI command
    app.cli.add_command(init_db_command)

    #initializing extensions
    db.init_app(app)
    migrate.init_app(app, db)

    from src.controllers import user
    app.register_blueprint(user.bp)
    
    return app

