class Vector(list):
    def __init__(self, storage):
        super(Vector, self).__init__(storage)

    def length(self):
        return sum([elem ** 2 for elem in self]) ** 0.5

    def normalize(self):
        return self * (1.0 / self.length())

    def __add__(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError("required a vector")
        if len(vector) != len(self):
            raise ArithmeticError("vector is not the same length")
        for i in xrange(len(self)):
            self[i] += vector[i]
        return self

    def __sub__(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError("required a vector")
        if len(vector) != len(self):
            raise ArithmeticError("vector is not the same length")
        for i in xrange(len(self)):
            self[i] -= vector[i]
        return self

    def __mul__(self, scalar):
        if not isinstance(scalar, (float, int, long)):
            raise TypeError("can't multiply vector by non-int of type " + type(scalar))
        for i in xrange(len(self)):
            self[i] *= scalar
        return self

    def __div__(self, scalar):
        if not isinstance(scalar, (float, int, long)):
            raise TypeError("can't divide vector by non-int of type " + type(scalar))
        for i in xrange(len(self)):
            self[i] /= scalar
        return self
