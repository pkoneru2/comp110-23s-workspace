"""Building Utility Functions"""

__author__ = "730570597"


def only_evens(input: list[int]) -> list[int]:
    """Returns even elements of list"""
    list1 = list()
    for idx in range(0, len(input)):
        if input[idx] % 2 == 0:
            list1.append(input[idx])
    return list1


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Concatenates two lists by adding second list to end of first"""
    for idx in range(0, len(list2)):
        list1.append(list2[idx])
    return list1


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Returns subset of list within range given by user"""
    list1 = list()
    if start < 0:
        start = 0
    if end > len(input):
        end = len(input)
    if len(input) == 0:
        return list1
    for idx in range(start, end):
        list1.append(input[idx])
    return list1
