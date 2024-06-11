# content of conftest.py
from test_foocompare import Foo


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return[
            "Comparing Foo instances:"
            f" vals: {left.val} != {right.val}",
        ]
