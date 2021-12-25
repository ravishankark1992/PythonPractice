# you may use the following libraries:
# import numpy;
# import pandas;
# import sklearn;

# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")
import numpy as np

img = np.zeros((20, 20))
pt1 = [4, 4]
pt2 = [12, 12]


def draw_rectangle(img, top_left, bottom_right):
    # top_left = x1, y1
    # bottom_right = x2, y2
    # check for edge cases
    x1, y1 = top_left
    x2, y2 = bottom_right
    for x in range(x1, x2 + 1):
        img[x, y1] = 1
        img[x, y2] = 1
    for y in range(y1 + 1, y2):
        img[x1, y] = 1
        img[x2, y] = 1
    # processing -> will be updating img

    return img


# updated_image = draw_rectangle(img, top_left=pt1, bottom_right=pt2)
# print(updated_image)
# print("")
# updated_img = draw_rectangle(updated_image, top_left=[6,6], bottom_right=[16,16])
# print(updated_image)
import math


def dist_fn(pt1, pt2):
    y1, x1 = pt1
    y2, x2 = pt2

    dist = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    return dist


centre_point = [6, 6]
radius = 4
blank_img = np.zeros((20, 20))


def draw_circle(img, centre_point, radius):
    # left quadrant to top point
    left_point = [centre_point[0], centre_point[1]-4]
    top_point = [centre_point[0]-4, centre_point[1]]
    centre_point = np.array(centre_point)
    print(left_point, top_point)
    current_point = left_point
    img[current_point] = 1
    n=0
    while current_point != top_point and n<100:
        print("current_point:", current_point)
        # cal distance of updated current point againt center
        right_dist = abs(dist_fn([current_point[0]+1, current_point[1]], centre_point) - radius)
        top_dist = abs(dist_fn([current_point[0], current_point[1]+1], centre_point) - radius)
        dist_list = [right_dist, top_dist]
        dir = dist_list.index(min(dist_list))
        print(right_dist, top_dist)
        if not dir:
            current_point = (current_point[0] + 1, current_point[1])
        else:
            current_point = (current_point[0], current_point[1] + 1)
        img[current_point] = 1
        n+=1
    return img


img = draw_circle(blank_img, centre_point, radius)
print(img)
