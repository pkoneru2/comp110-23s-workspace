def odd_and_even(input: list[int]) -> list[int]:
    list1: list[int] = list()
    for i in range (0, len(input)):
        if i % 2 == 0 and input[i] % 2 != 0:
            list1.append(input[i])
    return list1

print(odd_and_even([7, 8, 10, 10, 5, 12, 3, 2, 11, 8]))

def value_exists(input: dict[str, int], num: int) -> bool:
    num_check = False
    for i in input:
        if input[i] == num:
            num_check = True
    return num_check

test_dict: dict[str, int] = {"a": 2, "b": 4, "c": 7, "d": 1}
test_val = 5        
print(value_exists(test_dict, test_val))

def short_word(input: list[str]) -> list[str]:
    list1: list[int] = list()
    for i in input:
        if len(i) >= 5:
            print(f"{i} is too long!")
        elif len(i) < 5:
            list1.append(i)
    return list1

print(short_word(["sun", "cloud", "sky"]))
        