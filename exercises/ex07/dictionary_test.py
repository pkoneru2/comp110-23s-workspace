"""Unit tests for dictionary functions."""

__author__ = "730570597"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert1() -> None:
    """Edge Case: Tests Empty Dictionary."""
    assert invert({}) == {}


def test_invert2() -> None:
    """Use Case: Inverting UNC Basketball Dictionary."""
    test_dict: dict[str, str] = {"Michael": "Jordan", "Vince": "Carter", "James": "Worthy"}
    assert invert(test_dict) == {'Jordan': 'Michael', 'Carter': 'Vince', 'Worthy': 'James'}


def test_invert3() -> None:
    """Use Case: Inverting Current UNC Basketball Dictionary."""
    test_dict: dict[str, str] = {"Armando": "Bacot", "Leaky": "Black", "Caleb": "Love", "Pete": "Nance"}
    assert invert(test_dict) == {'Bacot': 'Armando', 'Black': 'Leaky', 'Love': 'Caleb', 'Nance': 'Pete'}


def test_favorite_color1() -> None:
    """Edge Case: Tests Empty Dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color2() -> None:
    """Use Case: My Suite's Favorite Colors."""
    test_dict: dict[str, str] = {"Troy": "red", "Vihit": "red", "Pranay": "green", "Roshan": "green", "Diamoah": "blue"}
    assert favorite_color(test_dict) == "red"


def test_favorite_color3() -> None:
    """Use Case: Star Wars Favorite Colors."""
    test_dict: dict[str, str] = {"Luke": "green", "Anakin": "blue", "Yoda": "green", "Obi-Wan": "blue", "Palpatine": "red"}
    assert favorite_color(test_dict) == "green"


def test_count1() -> None:
    """Edge Case: Tests Empty List."""
    assert count([]) == {}


def test_count2() -> None:
    """Use Case: Tests Food."""
    test_list: list[str] = ["Pizza", "Pasta", "Pizza", "Burger", "Cake", "Pasta", "Cake", "Legume", "Green Bean", "Cake", "Pizza", "Legume"]
    assert count(test_list) == {'Pizza': 3, 'Pasta': 2, 'Burger': 1, 'Cake': 3, 'Legume': 2, 'Green Bean': 1}


def test_count3() -> None:
    """Use Case: Tests Artists."""
    test_list: list[str] = ["Kanye", "Drake", "Taylor", "Kanye", "Kanye", "Kanye", "Drake", "Michael Jackson", "Michael Jackson", "Bob Ross", "Bob Ross"]
    assert count(test_list) == {'Kanye': 4, 'Drake': 2, 'Taylor': 1, 'Michael Jackson': 2, 'Bob Ross': 2}