import datetime
import os

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 是否启动DEBUG模式
DEBUG = True

# 密钥
SECRET_KEY = 'a\xce\xf4}\xa7,\xeb\xe3\xb3\x1eH\xa8\x82\xd8\xablR\x18\x1c\x06\x08\xb5\x14\xe5'

# 数据库连接
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@host:port/dbname?charset=utf8"
# 是否输出打印
SQLALCHEMY_ECHO = False
# 连接池配置
SQLALCHEMY_ENGINE_OPTIONS = {
    'echo_pool': True,
    'pool_size': 5,
    'max_overflow': 10,
    'pool_recycle': 30
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

# jwt 配置
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)

# 插件配置
PLUGINS = [
    "plugins.db:db_plugin",
    "plugins.cors:cors_plugin",
    "plugins.jwt_token:jwt_plugin"
]

# APP列表配置
APP_LIST = [
    "demo"
]
