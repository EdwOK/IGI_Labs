import numbers


class ObjectField(object):
    def __init__(self, default = None):
        self.obj = default

    def default_value(self):
        return self.obj

    def __str__(self):
        return str(self.default_value())

    def type(self):
        return type(self.default_value())


class StringField(ObjectField):
    def default_value(self):
        return basestring()

    def type(self):
        return basestring


class NumericField(ObjectField):
    def default_value(self):
        return 0

    def type(self):
        return numbers.Number


class BooleanField(ObjectField):
    def default_value(self):
        return False


class ListField(ObjectField):
    def default_value(self):
        return list()


class SetField(ObjectField):
    def default_value(self):
        return set()


class TupleField(ObjectField):
    def default_value(self):
        return tuple()


class DictField(ObjectField):
    def default_value(self):
        return dict()


