from core.main import Calculator
from contextlib import nullcontext as does_not_raise
import pytest


def test_main():
    assert 1 == 1


@pytest.mark.parametrize(
    'x, y, res',
    [
        (6, 2, 3),
        (10, -5, -2),
        (0, 5, 0),
    ]
)
def test_sum(x, y, res):
    assert Calculator.sum(x, y) == res


@pytest.mark.parametrize(
    'res, exception, x',
    [
        (14, does_not_raise(), (2, 3, 4, 5)),
        (3, does_not_raise(), (10, -5, -2)),
        (5, does_not_raise(), (0, 5, 0)),
        (5.5, pytest.raises(TypeError), (0, 5, 0.5)),
    ]
)
def test_sum_all(res, exception, x):
    with exception:
        assert Calculator.sum_all(*x) == res


@pytest.mark.parametrize(
    'x, y, res',
    [
        (6, 2, 3),
        (10, -5, -2),
        (0, 5, 0),
    ]
)
def test_divide(x, y, res):
    assert Calculator.divide(x, y) == res
