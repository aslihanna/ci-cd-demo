import pytest

from app import add, multiply


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (0, 0, 0),
        (1, 2, 3),
        (-1, 1, 0),
        (100, 250, 350),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (0, 0, 0),
        (1, 2, 2),
        (-1, 1, -1),
        (10, 5, 50),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
