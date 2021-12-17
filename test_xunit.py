from xunit import assert_equal, XUnitTestFailure, XUnitTestRunner


def test_can_run_test_function():
    was_run = False

    def test_function():
        nonlocal was_run
        was_run = True

    XUnitTestRunner().run_test_function(test_function)

    assert_equal(True, was_run)
    print("SUCCESS")


def test_assert_equal_raises_exception_on_unequal():
    try:
        assert_equal(86, 99)
        print("FAILURE")
    except XUnitTestFailure:
        print("SUCCESS")


def test_assert_equal_does_not_raise_exception_on_equal():
    try:
        assert_equal(42, 42)
        print("SUCCESS")
    except XUnitTestFailure:
        print("FAILURE")


if __name__ == "__main__":
    test_runner = XUnitTestRunner()
    test_runner.run_test_function(test_can_run_test_function)
    test_runner.run_test_function(test_assert_equal_raises_exception_on_unequal)
    test_runner.run_test_function(test_assert_equal_does_not_raise_exception_on_equal)
