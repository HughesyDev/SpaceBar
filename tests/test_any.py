import pytest


def adds_one(number: int) -> int:
    return number + 1


def test_adds_one_passing():
    assert adds_one(2) == 3


def test_adds_one_failing():
    # ARRANGE
    expected = adds_one(2) == 3
    # ACT
    actual = adds_one(2) == 50
    # ASSERT
    if expected != actual:
        assert pytest.raises(Exception)
