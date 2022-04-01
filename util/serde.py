from abc import ABCMeta, abstractmethod

from connexion.apps.flask_app import FlaskJSONEncoder


class ComplexObjectJSONEncoder(FlaskJSONEncoder):
    def default(self, o):
        if isinstance(o, DictSerializableMixin):
            return o.to_dict()
        elif isinstance(o, type):
            return o.__name__
        else:
            return super().default(o)


def serialize_object(o):
    return ComplexObjectJSONEncoder().encode(o)


class DictSerializableMixin(metaclass=ABCMeta):
    @abstractmethod
    def to_dict(self) -> dict:
        pass
