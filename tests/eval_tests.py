import unittest
from system.util import data_to_app
from system.objspace import symbol, eval, w_true, w_false, s_eq

if_ = symbol("if")
add_ = symbol("+")


class RunTest(unittest.TestCase):
    def test_data(self):
        for x in data:
            form, result = x
            form = data_to_app(form)
            result = data_to_app(result)

            assert s_eq(eval(form), eval(result)) is w_true



data = [
    [(if_, True, 1, 2), 1],
    [(if_, False, 1, 2), 2],
    [(add_, 1), 1],
    [(add_, 1, 2), 3],
    [(add_, 1, 2, 3), 6],
    [(add_,), 0],
]