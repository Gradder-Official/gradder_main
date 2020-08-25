class NoUserError(Exception):
    pass

class InvalidTypeException(Exception):
    r"""Raised when an argument does not match an expected value"""
    pass

class InvalidFormatException(Exception):
    r"""Raised when an argument to a setter does not match the expected format"""
    pass