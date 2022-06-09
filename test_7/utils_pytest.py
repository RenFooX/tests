import pytest

from test_7.main import Player


class TestPlayer:
    names = [
        'Ashly',
        "Swen",
        "Andy",
    ]

    points = [
        5,
        8,
        10,
    ]

    @pytest.mark.parametrize("name", names)
    def test_check_name(self, name):
        player = Player(name)
        assert player

    @pytest.mark.parametrize("point", points)
    def test_check_point(self, point):
        player = Player(point)
        assert player

    @pytest.mark.parametrize("point", points)
    def test_return_points(self, point):
        player_xae12 = Player("X Æ A-12")
        player_xae12.add_points(point)
        assert player_xae12.get_points() == point



