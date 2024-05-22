from flask import Flask
from flask_jwt_extended import JWTManager
from core.base import BasePlugin


class JWTPlugin(BasePlugin):

    def init(self, app: Flask):
        jwt = JWTManager(app=app)


jwt_plugin = JWTPlugin()
