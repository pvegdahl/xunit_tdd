from xunit import assert_equal, XUnitTestFailure, XUnitTestRunner, XUnitTestBase


class SpyTestRunner(XUnitTestRunner):
    def __init__(self):
        self.printed = []

    def print(self, text: str):
        self.printed.append(text)


class TestXUnitTestRunner(XUnitTestBase):
    def setup(self):
        self.spy_test_runner = SpyTestRunner()

    def test_can_run_test_function(self):
        was_run = False

        def test_function():
            nonlocal was_run
            was_run = True

        SpyTestRunner().run_test_function(test_function)

        assert_equal(True, was_run)

    def test_assert_equal_raises_exception_on_unequal(self):
        try:
            assert_equal(86, 99)
            print(
                "WARNING WARNING WARNING: assert_equals is broken and the rest of your tests are not trustworthy"
            )
        except XUnitTestFailure:
            pass

    def test_assert_equal_does_not_raise_exception_on_equal(self):
        assert_equal(42, 42)

    def test_print_success(self):
        def test_success():
            pass

        self.spy_test_runner.run_test_function(test_success)
        assert_equal(["[SUCCESS] test_success"], self.spy_test_runner.printed)

    def test_print_failure(self):
        def test_failure():
            assert_equal(42, 47)

        self.spy_test_runner.run_test_function(test_failure)
        assert_equal(
            ["[FAILURE] test_failure: Expected 42, got 47"],
            self.spy_test_runner.printed,
        )

    def test_print_exception(self):
        def test_exception():
            raise Exception("Whoops!")

        self.spy_test_runner.run_test_function(test_exception)
        assert_equal(
            ["[ERROR] test_exception: Exception('Whoops!')"],
            self.spy_test_runner.printed,
        )

    def test_run_tests_in_class(self):
        class TestClass(XUnitTestBase):
            test_not_a_function = 4

            def test_a(self):
                pass

            def test_b(self):
                pass

            def not_a_test(self):
                pass

        self.spy_test_runner.run_test_in_class(TestClass)

        assert_equal(
            ["[SUCCESS] test_a", "[SUCCESS] test_b"], self.spy_test_runner.printed
        )

    def test_run_tests_in_isolation(self):
        class TestClass(XUnitTestBase):
            init_call_count = 0

            def __init__(self):
                TestClass.init_call_count += 1

            def test_a(self):
                pass

            def test_b(self):
                pass

        SpyTestRunner().run_test_in_class(TestClass)
        assert_equal(2, TestClass.init_call_count)

    def test_setup(self):
        class TestClass(XUnitTestBase):
            calls = []

            def setup(self):
                TestClass.calls.append("setup")

            def test_failure(self):
                TestClass.calls.append("test_failure")
                assert_equal(40, 77)

            def test_success(self):
                TestClass.calls.append("test_success")

        SpyTestRunner().run_test_in_class(TestClass)
        assert_equal(["setup", "test_failure", "setup", "test_success"], TestClass.calls)

    def test_teardown(self):
        class TestClass(XUnitTestBase):
            calls = []

            def teardown(self):
                TestClass.calls.append("teardown")

            def test_failure(self):
                TestClass.calls.append("test_failure")
                assert_equal(40, 77)

            def test_success(self):
                TestClass.calls.append("test_success")

        SpyTestRunner().run_test_in_class(TestClass)
        assert_equal(["test_failure", "teardown", "test_success", "teardown"], TestClass.calls)


if __name__ == "__main__":
    XUnitTestRunner().run_test_in_class(TestXUnitTestRunner)
