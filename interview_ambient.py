import numpy as np
import math


def calc_center(person_bbox):
    x = (2 * person_bbox[0] + person_bbox[2]) / 2
    y = (2 * person_bbox[1] + person_bbox[3]) / 2
    return [x, y]


def distance_fn(center_1, center_2):
    return math.sqrt((center_2[1] - center_1[1]) ** 2 + (center_2[0] - center_1[0]) ** 2)


def crowd_count(people, threshold):
    """Count the number of crowds given the person bboxes.

    Args:
      people: list of [x, y, w, h] bounding boxes
      threshold: maximum distance between two people in a crowd

    Returns:
      int, number of crowds


    """
    crowd_counter = 0
    crowd_list = []
    people_center = []
    for person in people:
        center = calc_center(person)
        people_center.append(center)
    print(people_center)

    pair_look_up = {}

    for first_idx in range(len(people_center) - 1):
        for second_idx in range(first_idx + 1, len(people_center)):
            distance = distance_fn(people_center[first_idx], people_center[second_idx])
            # print(first_idx, second_idx, distance)
            pair_look_up[(first_idx, second_idx)] = distance
            if distance <= threshold:
                crowd_list.append([first_idx, second_idx])
    # print("crowd_list: ",len(crowd_list))
    print(pair_look_up)

    return len(crowd_list)

    def search(pair_look_up):
        queue = []
        visited = []

    return None
    # return crowd_counter


# A simple test case
people = [
    [1, 1, 2, 2],  # center = [2, 2]
    [1, 2, 2, 2],  # center = [2, 3]
    [5, 5, 4, 4],  # center = [7, 7]
    [6, 5, 4, 4],  # center = [8, 7]
]
threshold = 2.0
assert crowd_count(people, threshold) == 2

# Goal: Count number of crowds
# Crowd: defined by distance between the centroid of bboxs.
# Input: people, threshold
# output:

# Test cases:
# Edge cases