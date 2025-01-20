"""In this example, the append_first_fixture is an autouse fixture. Because
it happens automatically, both test are affected by it, even though neither
test requested it. That doesn't mean they can't be requested though; just
that it isn't necessary.
"""
# contents of test_append_2.py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return 'a'


# Arrange
@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry):
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]
