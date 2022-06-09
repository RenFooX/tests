import pytest
from main import ticket_price

parametrs = [(0, "Бесплатно"), (1, "Бесплатно"), (7, "100 рублей"), (18, "200 рублей"), (25, "300 рублей"),
             (60, "Бесплатно"), (0.5, "Бесплатно"), (-1, "Ошибка")]


@pytest.mark.parametrize("first, expected", parametrs)
def test_sum_price(first, expected):
    assert ticket_price(first) == expected
