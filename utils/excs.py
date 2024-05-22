class Error(Exception):
    pass


class ModuleImportError(Error):
    pass


class ApiError(Error):
    pass


class DataNotFound(ApiError):
    pass


class DataAlreadyExistError(ApiError):
    pass


class PasswordError(ApiError):
    pass


class TokenInvalidError(ApiError):
    pass


class TokenExpiredError(Error):
    pass
