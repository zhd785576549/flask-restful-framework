import datetime
import json
import os.path
from importlib import import_module
from utils import excs


def load_module(mod_path: str):
    """
    加载模块

    :param mod_path: [str] 需要加载的模块路径
    :return:
    """
    try:
        return import_module(mod_path)
    except ImportError as e:
        raise excs.ModuleImportError(e)


def load_module_obj(mod_path: str):
    """
    加载模块中的对象

    :param mod_path: [str] 模块路径, 例如: "module_path:obj_name"
    :return: [Object] 对象
    """
    module_path, obj_name = mod_path.split(":")
    mod = import_module(module_path)
    return getattr(mod, obj_name, None)


def trans_bool(val, default_val=False):
    """
    将字符串转化为bool

    :param val: [str] 需要转化的值
    :param default_val: [bool] 默认值
    :return: [bool] Bool值
    """
    try:
        if val == "true" or val == "True":
            return True
        elif val == "false" or val == "False":
            return False
        else:
            return default_val
    except:
        return default_val


def trans_int(val, default_val):
    """
    trans string to int.

    :param val: [str] 需要转化的值
    :param default_val: [str] 默认值
    :return: [int] 数值
    """
    try:
        return int(val)
    except:
        return default_val


def trans_str_list(val, s=","):
    """
    将字符串转化为字符串列表

    :param val: [str] 需要转化的值
    :param s: [str] 分隔符
    :return: [list] 字符串列表
    """
    try:
        _v_list = val.split(s)
        return [_v.strip() for _v in _v_list if _v]
    except:
        return []


def trans_json_list(val: str):
    """
    将字符串转化为json

    :param val: [str] 需要转化的值
    :return:
    """
    try:
        return json.loads(val)
    except:
        return []


def get_project_root_path() -> str:
    """
    获取项目根目录

    :return:
    """
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
