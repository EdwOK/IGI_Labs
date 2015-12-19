class DefaultDict(dict):
    def __init__(self, default_factory, **kwargs):
        dict.__init__(self, kwargs)
        self._default_factory = default_factory

    def __missing__(self, key):
        if self._default_factory is None:
            raise KeyError(key)
        self[key] = value = DefaultDict(self._default_factory)
        return value
