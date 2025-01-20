# contents of test_append_1.py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return 'a'


# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]
