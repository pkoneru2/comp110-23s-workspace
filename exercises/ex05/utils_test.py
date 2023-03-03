"""Testing functions from utils.py."""

__author__ = "730570597"

from exercises.ex05.utils import only_evens, sub, concat


def test_even1() -> None:
    """Edge Case: Tests empty list."""
    assert only_evens([]) == []


def test_even2() -> None:
    """Use Case: Tests positive and negative numbers."""
    test_list: list[int] = [-5, -37, 45, 68, 0, -2, -3, -8]
    assert only_evens(test_list) == [68, 0, -2, -8]


def test_even3() -> None:
    """Use Case: Tests list of numbers with varying values."""
    test_list: list[int] = [12, 7, 5986, 345, 88]
    assert only_evens(test_list) == [12, 5986, 88]


def test_concatenate1() -> None:
    """Edge Case: Tests empty lists."""
    assert concat([], []) == []


def test_concatenate2() -> None:
    """Use Case: Tests two lists of same length."""
    test_list1: list[int] = [-75, 83, 678, 564, -9]
    test_list2: list[int] = [56, 327, -98, 65, 3]
    assert concat(test_list1, test_list2) == [-75, 83, 678, 564, -9, 56, 327, -98, 65, 3]


def test_concatenate3() -> None:
    """Use Case: Tests two lists of differing lengths."""
    test_list1: list[int] = [57, 8, -46, 789]
    test_list2: list[int] = [64, -98, 5]
    assert concat(test_list1, test_list2) == [57, 8, -46, 789, 64, -98, 5]


def test_sub1() -> None:
    """Edge Case: Tests list with negative start point and end point greater than length of list."""
    test_list: list[int] = [3, 5, -6, 75, 981]
    assert sub(test_list, -5, 100) == [3, 5, -6, 75, 981]


def test_sub2() -> None:
    """Use Case: Test list with negative and positive numbers."""
    test_list: list[int] = [3, 67, 8556, 93, -85, -73, 5, 7]
    assert sub(test_list, 3, 6) == [93, -85, -73]


def test_sub3() -> None:
    """Use Case: Test list with only positive numbers."""
    test_list: list[int] = [43, 65, 8, 5]
    assert sub(test_list, 1, 3) == [65, 8]
