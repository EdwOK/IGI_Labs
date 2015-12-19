class Logger(object):
    def __init__(self):
        self._log_cached = []
        self.__set_log_format()
        self.__init_attrs()

    def to_log(self, func):
        def wrapper(*args, **kwargs):
            func_result, log_result = func(*args, **kwargs), ""
            if not self._log_format_name is None:
                log_result += "{} {}".format(self._log_format_name, func.__name__)
            if not self._log_format_args is None:
                log_result += " | {} {}".format(self._log_format_args, args)
            if not self._log_format_kwargs is None:
                log_result += " {} {}".format(self._log_format_kwargs, kwargs)
            if not self._log_format_result is None:
                log_result += " | {} {}".format(self._log_format_result, func_result)
            self._log_cached.append(log_result)
            return func_result

        return wrapper

    def __set_log_format(self, log_format=None):
        if log_format is None:
            log_format = ["name:", "args:", "kwargs:", "result:"]
        self._log_format_name = log_format[0]
        self._log_format_args = log_format[1]
        self._log_format_kwargs = log_format[2]
        self._log_format_result = log_format[3]

    def __init_attrs(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and attr_name != "log":
                self.__dict__[attr_name] = self.to_log(attr)

    def __str__(self):
        return "\n".join(self._log_cached)
