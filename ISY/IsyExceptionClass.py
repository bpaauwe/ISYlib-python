__all__ = [ 'IsyError', 'IsyCommandError', 'IsyNodeError',
	'IsyResponseError', 'IsyPropertyError', 'IsyValueError',
	'IsyPropertyValueError' ]


#
# The Following was lifted from other modules used as examples
#
class IsyError(Exception):
    """Base exception."""
    def __init__(self, msg, exception=None):
        """Creates an exception. The message is required, but the exception
        is optional."""
        self._msg = msg
        self._exception = exception
        Exception.__init__(self, msg)

    def getMessage(self):
        "Return a message for this exception."
        return self._msg

    def getException(self):
        "Return the embedded exception, or None if there was none."
        return self._exception

    def __str__(self):
        "Create a string representation of the exception."
        return self._msg

    def __getitem__(self, ix):
        """Avoids weird error messages if someone does exception[ix] by
        mistake, since Exception has __getitem__ defined."""
        raise AttributeError("__getitem__")


class IsyCommandError(IsyError):
    """General exception for command errors."""
    pass

class IsyNodeError(IsyError):
    """General exception for Node errors."""
    pass

class IsyResponseError(IsyError):
    """General exception for Node errors."""
    pass

class IsyPropertyError(IsyError):
    """General exception for Node errors."""
    pass

class IsyValueError(IsyError):
    """General exception for Node errors."""
    pass

class IsyPropertyValueError(IsyError):
    """General exception for Node errors."""
    pass

class IsyAttributeError(IsyError):
    """General exception for Node errors."""
    pass

#
# Do nothing
# (syntax check)
#
if __name__ == "__main__":
    import __main__
    print __main__.__file__
    print("syntax ok")
    exit(0)