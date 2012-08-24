import system.rt as rt

from system.core import Object, symbol, integer
from system.bool import w_true, w_false
from system.polymorphic_func import extend



def _get_idx(data_w, w_item, otherwise):
    for x in range(0, len(data_w), 2):
        if rt.equals(data_w[x], w_item) is w_true:
            return x
    return -1

tp_sym = symbol("system", "PersistentArrayMap")
class PersistentArrayMap(Object):
    def __init__(self, data_w, w_meta):
        self._data_w = data_w
        self._w_data = w_meta
    def type(self):
        return tp_sym



class Get(rt.Func):
    def __init__(self):
        pass
    def invoke2(self, a, b):
        return a.invoke2(b, None)
    def invoke3(self, a, b, c):
        idx = _get_idx(a._data_w, b)
        if idx == -1:
            return c
        return self._data_w[idx]

EMPTY = PersistentArrayMap([], None)

@extend(rt._assoc, tp_sym)
def assoc(self, k, v):
    idx = _get_idx(self._data_w, k)
    if rt.equal(self._data_w[idx + 1], v) is w_true:
        return self
    data = self._data_w[:]
    if idx != -1:
        data[idx + 1] = v
        return PersistentArrayMap(data, self._w_meta)

    data.extend([k, v])
    return PersistentArrayMap(data, self._w_meta)

@extend(rt.count, tp_sym)
def count(self):
    return integer(len(self._data_w))

rt._get.install(tp_sym, Get())