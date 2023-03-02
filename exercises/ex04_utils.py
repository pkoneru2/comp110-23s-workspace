"""List Utils"""

__author__ = "730570597"


def all(nums: list[int], input: int) -> bool:
    """Checks to see if all numbers in the list are the same as the given integer."""
    idx: int = 0
    if (len(nums) == 0):
        return False
    while (idx < len(nums)):
        if (nums[idx] != input):
            return False
        else:
            idx += 1
    return True


def max(input: list[int]) -> int:
    """Finds largest number in a list."""
    if (len(input) == 0):
        raise ValueError("max() arg is an empty list")
    idx: int = 0
    max_num: int = 0
    while (idx < len(input)):
        if (idx == 0): 
            max_num = input[idx]
        elif (input[idx] > max_num):
            max_num = input[idx]
        idx += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists are equal."""
    idx = 0
    compare_lists: bool
    if (len(list1) == 0 and len(list2) == 0):
        return True
    elif (len(list1) == 0 and len(list2) != 0 or len(list2) == 0 and len(list1) != 0):
        return False
    while (idx < len(list1) and idx < len(list2)):
        if (list1[idx] == list2[idx] and len(list1) == len(list2)):
            compare_lists = True
        else:
            compare_lists = False
        idx += 1
    return compare_lists