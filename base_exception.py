class BaseWebException(Exception):
    status_code = 503
    def __init__(self, message,  payload=None):
        Exception.__init__(self)
        self.message = message
        if self.status_code is not None:
            self.status_code = self.status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['code'] = self.status_code
        return rv