from copy import deepcopy
class FragileDict:
    def __init__(self, d=None):
        if d:
            self._data = deepcopy(d)
        else:
            self._data = {}
        self._lock = False
    def __enter__(self):
        self._tmp = deepcopy(self._data)
        self._lock = True
        return self
        
    def __exit__(self, exception_type, exception_val, trace):
        self._lock = False
        if exception_type is None:
            self._data = deepcopy(self._tmp)
            del self._tmp
        else:
            del self._tmp
            print('Exception has been suppressed.')
            return True
    def __contains__(self, key):
        if self._lock:
            return key in self._tmp
        return key in self._data
    def __getitem__(self, key):
        if self._lock:
            return self._tmp[key]
        return deepcopy(self._data[key])
    def __setitem__(self, key, value):
        if self._lock:
            self._tmp[key] = value
        else:
            raise RuntimeError("Protected state")
