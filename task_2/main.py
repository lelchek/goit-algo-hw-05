from typing import List, Tuple


def main(array: List[float], value: float) -> Tuple[int, float | None]:
    counter = 0
    low = 0
    high = len(array)

    while low < high:
        counter += 1
        median = (high - low) // 2 + low
        target = array[median]

        if target == value:
            return counter, target
        elif value < target:
            high = median
        else:
            low = median + 1

    return counter, None if high == len(array) else array[high]
