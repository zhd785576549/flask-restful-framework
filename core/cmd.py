import inspect
import os.path
import pkgutil
import sys
from argparse import ArgumentParser
from core.app import create_app

from utils import funcs
from core.base import BaseCommand


def get_sub_commands_from_packages(pkg_dir: str) -> list:
    """
    从指定的包下获取子命令

    :param pkg_dir: [str] 包地址
    :return:
    """
    _sub_command_module_list = []
    for loader, module_name, is_pkg in pkgutil.walk_packages([pkg_dir]):
        top_module_name = "scripts"
        if not is_pkg:
            _sub_command_module_list.append(funcs.import_module(f"{top_module_name}.{module_name}"))
    return _sub_command_module_list


class CmdManager:

    def __init__(self, argv):
        self.__argv = argv
        self.__sub_commands = {}

    def run_from_argv(self):
        _main_cmd = self.__argv[0]
        _root_dir = funcs.get_project_root_path()
        _script_path = os.path.join(_root_dir, "scripts")
        _sub_command_module_list = get_sub_commands_from_packages(_script_path)
        _parser = ArgumentParser()
        for _sub_command_module in _sub_command_module_list:
            _members = inspect.getmembers(_sub_command_module, inspect.isclass)
            for _member in _members:
                _name, _cls = _member
                if _name == "BaseCommand":
                    continue

                if issubclass(_cls, BaseCommand):
                    if _cls.command_name:
                        self.__sub_commands[_cls.command_name] = _cls
        if len(self.__argv) == 1:
            self.print_helper()
            exit(0)
        _sub_command_name = self.__argv[1]
        _sub_command_cls = self.__sub_commands.get(_sub_command_name)
        if _sub_command_cls is None:
            self.print_helper()
            exit(-1)
        if _sub_command_cls.need_init_app is True:
            _app = create_app(__name__)
        else:
            _app = None
        _sub_command_cls(app=_app).run(_parser)

    def print_helper(self):
        """
        打印帮助信息

        :return:
        """
        print("Usage: python run.py [sub_command] --help")
        print(f"Available sub commands: ")
        for _k, _cls in self.__sub_commands.items():
            print(f"{_k}\t\t {_cls.helper}")


def run_from_argv():
    """
    执行命令

    :return:
    """
    CmdManager(sys.argv).run_from_argv()
