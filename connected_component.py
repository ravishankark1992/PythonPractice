"""/ *Given
a
2
d
matrix(image)
with white pixels(pixel value 1)
and black
pixels(pixel
value
0), count
the
number
of
blobs
with white pixels.A blob is a group of pixels that are
connected
horizontally or vertically.

Example
1:

Input:
11110
11010
11000
00000

Output: 1

Example
2:

Input:
11000
11000
00100
00011

Output: 3 * /
"""
"""
Algorithm steps
1. read image, obtain dimension
2. start from one of the vertices, iterate over the pixels (x/y directions)
3. Iterate until we have pixel 0. 
4. Once we reach pixel value 1, Add 1 to the counter to keep track of number of blobs, start search for connected components that are 1s.
5. Iterate until we reach end of connected 1s. If all pixels are done for this blob, Exit blob search, 
Continue with rest of the image to iterate for more blobs.
6. Return blob counter.
#
"""

import numpy as np


class BlobCountingAlgorithm:
    def __init__(self, image):
        self.visited = []
        self.blob_counter_value = 0
        self.dfs_queue = []
        self.height = 0
        self.width = 0
        self.image = image

    def blob_counter(self, image) -> int:
        self.width, self.height = np.shape(image)
        row = 0
        while row < self.width:
            col = 0
            while col < self.height:
                if (row,col) in self.visited:
                    col+=1
                    continue
                if image[row][col] == 0:
                    self.visited.append((row, col))
                else:
                    self.blob_counter_value += 1
                    self.visited.append((row, col))
                    self.dfs_queue.append((row, col))
                    self.dfs(row, col)
                col += 1
            row += 1
        return self.blob_counter_value

    def explore_children(self, row, col):
        if self.width > row + 1 and (row + 1, col) not in self.visited and (
                row + 1, col) not in self.dfs_queue and self.image[row + 1][col] == 1:
            self.dfs_queue.append((row + 1, col))
        if self.height > col + 1 and (row, col + 1) not in self.visited and (
                row, col + 1) not in self.dfs_queue and self.image[row][col + 1] == 1:
            self.dfs_queue.append((row, col + 1))
        if row - 1 >= 0 and (row - 1, col) not in self.visited and (row - 1, col) not in self.dfs_queue and \
                self.image[row - 1][col] == 1:
            self.dfs_queue.append((row - 1, col))
        if col - 1 >= 0 and (row, col - 1) not in self.visited and (row, col - 1) not in self.dfs_queue and \
                self.image[row][col - 1] == 1:
            self.dfs_queue.append((row, col - 1))
        return

    def dfs(self, row, col):
        self.explore_children(row, col)
        if len(self.dfs_queue) > 0:
            row, col = self.dfs_queue.pop(-1)
            self.visited.append((row, col))
            self.dfs(row, col)


def main():
    image = [[0, 1, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 1, 1, 1]]
    # image = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    counter_object = BlobCountingAlgorithm(image)
    blob_counter_value = counter_object.blob_counter(image)
    print(blob_counter_value)

# Imput image: image= [[]]
main()
