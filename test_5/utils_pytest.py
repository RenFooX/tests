import pytest

from test_5.main import get_period

parameters = [
    (5, 'ночь'),
    (10, 'утро'),
    (15, 'день'),
    (20, 'вечер'),
]

garde_exceptions = [
    (-1, ValueError),
    (25, ValueError),
    ("5", TypeError),
    (5.0, TypeError),
]


@pytest.mark.parametrize("grade_int, grade_str", parameters)
def test_get_verbal_grade(grade_int, grade_str):
    assert get_period(grade_int) == grade_str


@pytest.mark.parametrize("grade_int, exception", garde_exceptions)
def test_get_verbal_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        get_period(grade_int)
