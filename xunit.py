from typing import Callable, Any, Type


class XUnitTestFailure(Exception):
    pass


def assert_equal(expected: Any, actual: Any):
    if expected != actual:
        raise XUnitTestFailure(f"Expected {expected}, got {actual}")


class XUnitTestRunner:
    def run_test_function(self, test_function: Callable):
        try:
            test_function()
            self.print(f"[SUCCESS] {test_function.__name__}")
        except XUnitTestFailure as assertion_failure:
            self.print(f"[FAILURE] {test_function.__name__}: {assertion_failure}")
        except Exception as e:
            self.print(f"[ERROR] {test_function.__name__}: {repr(e)}")

    def print(self, text: str):
        print(text)

    def run_test_in_class(self, test_class: Type[object]):
        pass
