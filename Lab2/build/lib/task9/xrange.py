class XRange(object):
    def __init__(self, *args):
        if len(args) == 1:
            start, stop, step = 0, args[0], 1
        elif len(args) == 2:
            start, stop, step = args[0], args[1], 1
        elif len(args) == 3:
            start, stop, step = args

        self._step = step
        self._start = start
        self._stop = (stop - start) // step + bool((stop - start) % step)

    def __iter__(self):
        count = 0
        while count < self._stop:
            yield self._start
            self._start += self._step
            count += 1
