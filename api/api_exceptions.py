from base_exception import BaseWebException


class BaseApiException(BaseWebException):
    status_code = 400


class InvalidArgument(BaseApiException):
    pass