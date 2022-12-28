import numpy as np


def return_second_highest(input):
    highest = input[0]
    second_highest = input[0]
    for i in range(1, len(input)):

        if input[i] > highest:
            second_highest = highest
            highest = input[i]
        elif input[i] != highest and input[i] > second_highest:
            second_highest = input[i]
    return highest, second_highest


l1 = [7, 9, 8, 11, 16, 15, 0, -2, 2.5, 5]
second = return_second_highest(l1)
print(second)
