from fields import *


class ModelCreator(type):
    def __call__(cls, *args, **kwargs):
        new_class = type.__call__(cls, *args)
        for key, value in kwargs.iteritems():
            if hasattr(new_class, key):
                attr = getattr(new_class, key)
                if issubclass(type(attr), ObjectField):
                    if not issubclass(type(value), attr.type()):
                        raise TypeError('Excepted type {} not found'.format(key))
                    setattr(new_class, key, value)
            else:
                raise TypeError('No {} attr found'.format(key))
        return new_class
