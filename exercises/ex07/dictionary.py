"""Dictionary Functions Practice."""

__author__ = "730570597"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in a dictionary."""
    dict1: dict[str, str] = dict()
    for i in input:
        if (input[i] in dict1):
            raise KeyError("KeyError: Cannot have duplicate keys")    
        else:
            dict1[input[i]] = i
    return dict1


def favorite_color(input: dict[str, str]) -> str:
    """Counts how many times a color appears and outputs most frequently occurring color."""
    color: str = ""
    count: int = 0
    dict1: dict[str, int] = dict()
    for i in input:
        if (input[i] in dict1):
            dict1[input[i]] += 1
        else:
            dict1[input[i]] = 1
    for i in dict1:
        if (dict1[i] > count):
            count = dict1[i]
            color = i
    return color


def count(input: list[str]) -> dict[str, int]:
    """Measures frequency of elements in a list and inputs values into dictionary with elemnts as keys and frequencies as values."""
    dict1: dict[str, int] = dict()
    for i in input:
        if (i in dict1):
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1