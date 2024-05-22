from functools import wraps
from utils import excs
from utils.resp import RespUtils


def exception_wrap(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except excs.DataNotFound:
            import traceback
            traceback.print_exc()
            return RespUtils.not_found()
        except excs.DataAlreadyExistError as e:
            return RespUtils.data_already_exist(str(e))
        except Exception as e:
            import traceback
            return RespUtils.inner_error(msg=traceback.format_exc())
    return inner
