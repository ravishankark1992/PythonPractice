from typing import List, Dict
from argparse import ArgumentParser
import numpy as np


class BinarySearch:
    def search(self, key: int, input_list: list):
        low = 0
        high = len(input_list) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if key == input_list[mid]:
                return mid
            elif key < input_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == "__main__":
    # sorted_list = list(np.sort(np.random.randint(1, 64, 15)))
    key = 42
    sorted_list = [3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]
    bs = BinarySearch()
    print(sorted_list, key)
    print(bs.search(key, sorted_list))
