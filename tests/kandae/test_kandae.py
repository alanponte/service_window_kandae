import pytest

from kandae.kandae import smallest_sum_subarr


@pytest.mark.parametrize(
    "input, expected", [
        ([3, -4, 2, -3, -1, 7, -5], ((-6, 1, 4)))
    ]
)
def test_kandae(input, expected):
    assert smallest_sum_subarr(arr=input) == expected
