"""In testing, a fixture provides a defined, reliable and consistent context for
the tests. This could include environment(for example a database configured with
known parameters) or content (such as a dataset).

Fixtures define the steps and data that constitute the 'arrange' phade of a
test. In Pytest, they are functions you define that serve this purpose. They can
also be used to define a test's act phase; this is a powerful technique for
designing moer complex tests.

The servises, state, or other operating environments set up by fixtures are
accessed by test functions through arguments. For each fixtures used by a test
function there is typically a parameter(named after the fixture) in the test
function's definition.

We can tell Pytest that  particular function is a fixture by decorating it with
@pytest.fixture. Here's a simple example of what a fixture in pytest might look
like:"""
import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit('apple')


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
