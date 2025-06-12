from main import add
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
    ],
)
def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected, f"Expected {expected}, but got {result}"
