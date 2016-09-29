class fibs:
    _vals = [0, 1]

    def __call__(self, n):
        while n >= len(self._vals):
            self._vals.append(sum(self._vals[-2:]))
        return self._vals[-1]

fibs = fibs()

