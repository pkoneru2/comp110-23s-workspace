def zip(input1: list[str], input2: list[int]) -> dict[str, int]:
    dictionary: dict[str, int] = {}
    if(len(input1) == 0 or len(input2) == 0):
        return dictionary
    if (len(input1) != len(input2)):
        return dictionary
    idx: int = 0
    while (idx < len(input1)):
        dictionary[input1[idx]] = input2[idx]
        idx += 1
    return dictionary
