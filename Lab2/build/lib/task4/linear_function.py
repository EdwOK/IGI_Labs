class LinearFunction(object):
    def __init__(self, k=1, b=0):
        self._k = k
        self._b = b

    def __call__(self, other):
        if isinstance(other, LinearFunction):
            try:
                self._b += self._k * other._b
                self._k *= other._k
                return self
            except TypeError:
                print("In the value of the argument requires function")
        else:
            return self._k * other + self._b

    def __add__(self, func):
        if not isinstance(func, LinearFunction):
            raise TypeError("required a linear function")
        self._k += func._k
        self._b += func._b
        return self

    def __mul__(self, scalar):
        if not isinstance(scalar, (float, int, long)):
            raise TypeError("required a number")
        self._k *= scalar
        self._b *= scalar
        return self

    def __str__(self):
        return "y = {0}x + {1}".format(self._k, self._b)