import pytest

from test_3.main import get_verbal_grade

grade_parameters = [
    (2, "Плохо"),
    (3, "Удовлетворительно"),
    (4, "Хорошо"),
    (5, "Отлично"),
]


grade_exceptions = [
    (1, ValueError),
    (6, ValueError),
    ("5", TypeError),
    (5.0, TypeError),
]


@pytest.mark.parametrize("grade_int, grade_str", grade_parameters)
def test_get_verbal_grade(grade_int, grade_str):
    assert get_verbal_grade(grade_int) == grade_str


@pytest.mark.parametrize("grade_int, exception", grade_exceptions)
def test_get_verbal_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        get_verbal_grade(grade_int)


def test_get_verbal_grade_value_error_1():
    with pytest.raises(ValueError):
        get_verbal_grade(1)


def test_get_verbal_grade_value_error_6():
    with pytest.raises(ValueError):
        get_verbal_grade(6)


def test_get_verbal_grade_type_error_str():
    with pytest.raises(TypeError):
        get_verbal_grade("5")


def test_get_verbal_grade_type_error_floart():
    with pytest.raises(TypeError):
        get_verbal_grade(5.0)
