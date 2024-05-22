class RespCode:
    OK = 2000
    AUTH_FAILED = 3001
    PASSWORD_ERROR = 3003
    PARAM_INVALID = 4000
    NOT_FOUND = 4004
    DATA_ALREADY_EXIST = 4005
    ALREADY_EXPIRED = 4009
    INNER_ERROR = 9999


class Resp:

    def __init__(self, code: int, msg: str, data: any = None):
        self.__code = code
        self.__msg = msg
        self.__data = data

    def to_dict(self):
        return {
            "code": self.__code,
            "msg": self.__msg,
            "data": self.__data
        }


class RespUtils:

    @staticmethod
    def ok(data=None):
        return Resp(code=RespCode.OK, msg="ok", data=data).to_dict()

    @staticmethod
    def auth_failed():
        return Resp(code=RespCode.AUTH_FAILED, msg="Auth failed.").to_dict()

    @staticmethod
    def inner_error(msg="Server error."):
        return Resp(code=RespCode.INNER_ERROR, msg=msg).to_dict()

    @staticmethod
    def not_found():
        return Resp(code=RespCode.NOT_FOUND, msg="Data not found").to_dict()

    @staticmethod
    def data_already_exist(msg="Data already exist."):
        return Resp(code=RespCode.DATA_ALREADY_EXIST, msg=msg).to_dict()

    @staticmethod
    def already_expired():
        return Resp(code=RespCode.ALREADY_EXPIRED, msg="Already expired.").to_dict()

    @staticmethod
    def param_invalid(msg="Param invalid."):
        return Resp(code=RespCode.PARAM_INVALID, msg=msg).to_dict()

    @staticmethod
    def password_error():
        return Resp(code=RespCode.PASSWORD_ERROR, msg="密码错误").to_dict()
