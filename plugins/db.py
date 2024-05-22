from flask import Flask

from core.base import BasePlugin
from flask_sqlalchemy import SQLAlchemy


class DatabasePlugin(BasePlugin):

    def __init__(self):
        super().__init__()

        self.__db = SQLAlchemy()

    def init(self, app: Flask):
        self.__db.init_app(app=app)

    @property
    def db(self) -> SQLAlchemy:
        return self.__db


db_plugin = DatabasePlugin()
