from xunit import run_test_function


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


if __name__ == "__main__":
    run_test_function(test_can_run_test_function)
