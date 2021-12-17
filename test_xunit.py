from xunit import run_test_function, assert_equal, XUnitTestFailure


def test_can_run_test_function():
    was_run = False

    def test_function():
        nonlocal was_run
        was_run = True

    run_test_function(test_function)

    if was_run:
        print("SUCCESS")
    else:
        print("FAILURE")


def test_assert_equal_raises_exception_on_unequal():
    try:
        assert_equal(86, 99)
        print("FAILURE")
    except XUnitTestFailure:
        print("SUCCESS")


if __name__ == "__main__":
    run_test_function(test_can_run_test_function)
    run_test_function(test_assert_equal_raises_exception_on_unequal)
