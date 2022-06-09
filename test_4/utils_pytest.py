import pytest

from test_4.main import get_grade

parametrs = [
    (10, 2),
    (10, 2),
    (30, 3),
    (70, 4),
    (100, 5),
]

_param = [
    (-1, ValueError),
    ("1", TypeError),
    (101, ValueError),
]

@pytest.mark.parametrize("score, point", parametrs)
def test_check(score, point):
    assert get_grade(score) == point


@pytest.mark.parametrize("score, exception", _param)
def test_check_2(score, exception):
    with pytest.raises(exception):
        get_grade(score)
