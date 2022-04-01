from logging import getLogger


class LoggingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._log = getLogger(f'{self.__class__.__module__}.{self.__class__.__name__}')

    @property
    def logger(self):
        return self._log