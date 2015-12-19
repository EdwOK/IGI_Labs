class Enumerable(object):
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return iter(self._collection)

    def where(self, func):
        return [elem for elem in self if func(elem)]
