from abc import ABC, abstractmethod
from flask import Flask
from argparse import ArgumentParser


class BasePlugin(ABC):

    @abstractmethod
    def init(self, app: Flask):
        """
        Initializer plugin abstract method.

        eg:
            DatabasePlugin(BasePlugin):

                def init(self, app):
                    self.__db = Sqlalchemy(app=app)

            Register in PLUGIN_LIST of settings, while be initialized automatically.
            PLUGIN_LIST = [
                ...,
                "plugins.db:db_handler"
            ]
        :param app: [Flask] Object of FLask
        :return:
        """


class BaseCommand(ABC):
    command_name = None
    helper = ""
    need_init_app = True

    def get_name(self) -> str:
        """
        获取二级命令的名称

        :return: [str] 二级命令的名称
        """

    def __init__(self, app: Flask):
        self.__app = app

    def add_parser(self, parser):
        """
        添加参数解析

        :return: [ArgumentParser] 返回参数解析器
        """

    def run(self, parser: ArgumentParser):
        sub_parsers = parser.add_subparsers()
        sub_parser = sub_parsers.add_parser(self.command_name, help=self.helper)
        self.add_parser(parser=sub_parser)
        args = parser.parse_args()
        if self.__app:
            with self.__app.app_context():
                self.handle_run(**vars(args))
        else:
            self.handle_run(**vars(args))

    @abstractmethod
    def handle_run(self, **kwargs):
        """
        Handler command body
        :param kwargs: [dict] Command params.
        :return:
        """

    @property
    def app(self) -> Flask:
        return self.__app
