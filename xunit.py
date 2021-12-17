from typing import Callable, Any


class XUnitTestFailure(Exception):
    pass


def assert_equal(expected: Any, actual: Any):
    if expected != actual:
        raise XUnitTestFailure()


class XUnitTestRunner:
    def run_test_function(self, test_function: Callable):
        test_function()
