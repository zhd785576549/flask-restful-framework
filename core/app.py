import warnings

from flask import Flask, Blueprint
import os
from utils import funcs
from utils import excs
from core.base import BasePlugin


def load_settings(app: Flask):
    """
    根据环境加载配置信息

    :param app: [Flask] Flask应用对象
    :return:
    """
    env = os.environ.get("FLASK_APP", "dev")
    _settings_module_path = f"conf.{env}_settings"
    try:
        _settings_obj = funcs.import_module(_settings_module_path)
        app.config.from_object(_settings_obj)
    except excs.ModuleImportError:
        warnings.warn(f"""
        Cannot find settings frm env : {env}, program will exist -1.
        """)
        exit(-1)


def load_plugins(app: Flask):
    """
    加载插件

    :param app: [Flask] Flask应用对象
    :return:
    """
    plugins = app.config.get("PLUGINS", [])
    for plugin in plugins:
        _plugin_obj = funcs.load_module_obj(mod_path=plugin)
        if _plugin_obj and isinstance(_plugin_obj, BasePlugin):
            _plugin_obj.init(app=app)


def load_apps(app: Flask):
    """
    加载应用列表

    :param app: [Flask] Flask应用对象
    :return:
    """
    app_list = app.config.get("APP_LIST", [])
    api_blueprinter = Blueprint("admin", import_name=__name__)
    for _app_str in app_list:
        _app_url_mod_str = f"apps.{_app_str}.urls"
        _app_mod = funcs.import_module(_app_url_mod_str)
        if hasattr(_app_mod, "urlpatterns"):
            _blueprint = getattr(_app_mod, "urlpatterns")
            _app_name = _app_str.replace(".", "/")
            if isinstance(_blueprint, Blueprint):
                api_blueprinter.register_blueprint(_blueprint, url_prefix=_app_name)
    app.register_blueprint(api_blueprinter, url_prefix="/admin")
    print(app.url_map)


def create_app(import_name) -> Flask:
    """
    创建Flask应用

    :param import_name: [str] 引入模块路径
    :return: [Flask] Flask应用对象
    """
    _app = Flask(import_name=import_name)

    # Load settings by env.
    load_settings(app=_app)

    # Load apps urls
    load_apps(app=_app)

    # Load plugins
    load_plugins(app=_app)

    return _app
