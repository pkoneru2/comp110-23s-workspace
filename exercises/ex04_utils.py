"""List Utils"""

__author__ = "730570597"

def all(nums: list[int], input: int) -> bool:
    idx: int = 0
    while (idx < len(nums)):
        if (nums[idx] == input):
            return True
        else:
            idx += 1
    return False

def max(input: list[int]) -> int:
    if (len(input) == 0):
        raise ValueError("max() arg is an empty list")
    idx: int = 0
    max_num: int = 0
    while (idx < len(input)):
        if (idx == 0):
            max_num = input[idx]
        elif(input[idx] > max_num):
            max_num = input[idx]
        idx += 1
    return max_num

def is_equal(list1: list[int], list2: list[int]) -> bool:
    idx = 0
    compare_lists: bool
    while (idx < len(list1) and idx < len(list2)):
        if (list1[idx] == list2[idx]):
            compare_lists = True
        else:
            compare_lists = False
        idx += 1
    return compare_lists

