from typing import Callable, Any


class XUnitTestFailure(Exception):
    pass


def run_test_function(test_function: Callable):
    test_function()


def assert_equal(expected: Any, actual: Any):
    raise XUnitTestFailure()
