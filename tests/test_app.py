import pytest

from app import add


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
