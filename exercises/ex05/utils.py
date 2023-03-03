"""Building Utility Functions"""

__author__ = "730570597"


def only_evens(input: list[int]) -> list[int]:
    """Returns even elements of list"""
    list1 = list()
    for idx in range(0, len(input)):
        if input[idx] % 2 == 0:
            list1.append(input[idx])
    return list1


def concat(input1: list[int], input2: list[int]) -> list[int]:
    """Concatenates two lists by adding second list to end of first"""
    list1 = list()
    for idx in range(0, len(input1)):
        list1.append(input1[idx])
    for idx in range(0, len(input2)):
        list1.append(input2[idx])
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

print(concat([1, 2, 3, 4], [1, 2 ,3, 4]))