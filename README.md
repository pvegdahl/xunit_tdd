# xunit_tdd
I built a basic XUnit style test framework using TDD as a learning exercise.  The test framework is used to test itself, which fun and mind-bending exercise.  This code is all about the journey, not the final product.  Don't use this for your testing.  Use pytest.

This code doesn't have any dependencies outside of Python itself.  You can run the tests with python test_xunit.py.  Any semi-recent version of python should be work.

I took the time to leave a very clean git history.  Each commit does exactly one of four things:
  1) Adds a failing test. (RED)
  2) Updates the production code to make the failing test pass. (GREEN)
  3) Refactors production code without changing any features. (REFACTOR)
  4) Refactor our test code to use a new feature of the test framework. (DOG FOOD)

There is no perfect order of tests (features), but after doing this exercise a number of times, I settled on the following order:
  1) Run an input (test) function
  2) Add an assert_equal function that raises an exception on unequal
  3) Assert_equal should not raise an exception on equal
  4) Record "success" for each passing test
  5) Include the test name in the success message
  6) Record "failure" and test name for each failing test
  7) Include a failure message (context) for failing tests
  8) Record tests that end with exceptions
  9) Run all functions in an input test class
  10) Do not run non-test functions in a test class
  11) Ensure that all tests in a test class run in isolation
  12) Support a test class setup function
  13) Support a test class teardown function

There are any number of additional features you could add.  This seemed like a good stopping point for the purpose of this exercise.

Hat tip to Kent Beck's TDD book for this idea.  I learned a lot by doing this exercise multiple times.
